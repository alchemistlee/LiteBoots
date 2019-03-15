# coding = utf-8

# @time    : 2019/2/19 5:42 PM
# @author  : alchemistlee
# @fileName: my_pred_server.py
# @abstract:

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from tensor2tensor.bin import t2t_trainer
from tensor2tensor.data_generators import problem  # pylint: disable=unused-import
from tensor2tensor.data_generators import text_encoder
# from tensor2tensor.utils import decoding
from tensor2tensor.utils import registry
from tensor2tensor.utils import trainer_lib
from tensor2tensor.utils import usr_dir

import pred_util as decoding

import tensorflow as tf



flags = tf.flags
FLAGS = flags.FLAGS

# Additional flags in bin/t2t_trainer.py and utils/flags.py
flags.DEFINE_string("checkpoint_path", None,
                    "Path to the model checkpoint. Overrides output_dir.")
flags.DEFINE_bool("keep_timestamp", False,
                  "Set the mtime of the decoded file to the "
                  "checkpoint_path+'.index' mtime.")
flags.DEFINE_bool("decode_interactive", False,
                  "Interactive local inference mode.")
flags.DEFINE_integer("decode_shards", 1, "Number of decoding replicas.")
flags.DEFINE_string("score_file", "", "File to score. Each line in the file "
                    "must be in the format input \t target.")
flags.DEFINE_bool("decode_in_memory", False, "Decode in memory.")


def create_hparams():
  return trainer_lib.create_hparams(
      FLAGS.hparams_set,
      FLAGS.hparams,
      data_dir=os.path.expanduser(FLAGS.data_dir),
      problem_name=FLAGS.problem)


def create_decode_hparams():
  decode_hp = decoding.decode_hparams(FLAGS.decode_hparams)
  decode_hp.shards = FLAGS.decode_shards
  decode_hp.shard_id = FLAGS.worker_id
  decode_hp.decode_in_memory = FLAGS.decode_in_memory
  decode_hp.decode_to_file = FLAGS.decode_to_file
  decode_hp.decode_reference = FLAGS.decode_reference
  return decode_hp

def my_decode(estimator, hparams, decode_hp,input_str):
  return decoding.decode_my_data(estimator,input_str, hparams, decode_hp,
                                  checkpoint_path=FLAGS.checkpoint_path)


def decode(estimator, hparams, decode_hp):
  """Decode from estimator. Interactive, from file, or from dataset."""
  if FLAGS.decode_interactive:
    if estimator.config.use_tpu:
      raise ValueError("TPU can only decode from dataset.")
    decoding.decode_interactively(estimator, hparams, decode_hp,
                                  checkpoint_path=FLAGS.checkpoint_path)
  elif FLAGS.decode_from_file:
    if estimator.config.use_tpu:
      raise ValueError("TPU can only decode from dataset.")
    decoding.decode_from_file(estimator, FLAGS.decode_from_file, hparams,
                              decode_hp, FLAGS.decode_to_file,
                              checkpoint_path=FLAGS.checkpoint_path)
    if FLAGS.checkpoint_path and FLAGS.keep_timestamp:
      ckpt_time = os.path.getmtime(FLAGS.checkpoint_path + ".index")
      os.utime(FLAGS.decode_to_file, (ckpt_time, ckpt_time))
  else:
    decoding.decode_from_dataset(
        estimator,
        FLAGS.problem,
        hparams,
        decode_hp,
        decode_to_file=FLAGS.decode_to_file,
        dataset_split="test" if FLAGS.eval_use_test_set else None)


def score_file(filename):
  """Score each line in a file and return the scores."""
  # Prepare model.
  hparams = create_hparams()
  encoders = registry.problem(FLAGS.problem).feature_encoders(FLAGS.data_dir)
  has_inputs = "inputs" in encoders

  # Prepare features for feeding into the model.
  if has_inputs:
    inputs_ph = tf.placeholder(dtype=tf.int32)  # Just length dimension.
    batch_inputs = tf.reshape(inputs_ph, [1, -1, 1, 1])  # Make it 4D.
  targets_ph = tf.placeholder(dtype=tf.int32)  # Just length dimension.
  batch_targets = tf.reshape(targets_ph, [1, -1, 1, 1])  # Make it 4D.
  features = {
      "inputs": batch_inputs,
      "targets": batch_targets,
  } if has_inputs else {"targets": batch_targets}

  # Prepare the model and the graph when model runs on features.
  model = registry.model(FLAGS.model)(hparams, tf.estimator.ModeKeys.EVAL)
  _, losses = model(features)
  saver = tf.train.Saver()

  with tf.Session() as sess:
    # Load weights from checkpoint.
    ckpts = tf.train.get_checkpoint_state(FLAGS.output_dir)
    ckpt = ckpts.model_checkpoint_path
    saver.restore(sess, ckpt)
    # Run on each line.
    with tf.gfile.Open(filename) as f:
      lines = f.readlines()
    results = []
    for line in lines:
      tab_split = line.split("\t")
      if len(tab_split) > 2:
        raise ValueError("Each line must have at most one tab separator.")
      if len(tab_split) == 1:
        targets = tab_split[0].strip()
      else:
        targets = tab_split[1].strip()
        inputs = tab_split[0].strip()
      # Run encoders and append EOS symbol.
      targets_numpy = encoders["targets"].encode(
          targets) + [text_encoder.EOS_ID]
      if has_inputs:
        inputs_numpy = encoders["inputs"].encode(inputs) + [text_encoder.EOS_ID]
      # Prepare the feed.
      feed = {
          inputs_ph: inputs_numpy,
          targets_ph: targets_numpy
      } if has_inputs else {targets_ph: targets_numpy}
      # Get the score.
      np_loss = sess.run(losses["training"], feed)
      results.append(np_loss)
  return results

estimator = None
hp=None
decode_hp=None

def entry(argv,input_str):
  global estimator
  global hp
  global decode_hp
  flags.FLAGS(argv , known_only=True)

  tf.logging.set_verbosity(tf.logging.INFO)
  trainer_lib.set_random_seed(FLAGS.random_seed)
  usr_dir.import_usr_dir(FLAGS.t2t_usr_dir)

  print("####")
  print(str(FLAGS.data_dir))
  print(str(FLAGS.problem))
  print(str(FLAGS.model))
  print(str(FLAGS.hparams_set))
  print(str(FLAGS.output_dir))
  print(str(FLAGS.decode_hparams))

  # if FLAGS.score_file:
  #   filename = os.path.expanduser(FLAGS.score_file)
  #   if not tf.gfile.Exists(filename):
  #     raise ValueError("The file to score doesn't exist: %s" % filename)
  #   results = score_file(filename)
  #   if not FLAGS.decode_to_file:
  #     raise ValueError("To score a file, specify --decode_to_file for results.")
  #   write_file = tf.gfile.Open(os.path.expanduser(FLAGS.decode_to_file), "w")
  #   for score in results:
  #     write_file.write("%.6f\n" % score)
  #   write_file.close()
  #   return

  if hp is None:
    hp = create_hparams()
  if decode_hp is None:
    decode_hp = create_decode_hparams()
  if estimator is None:
    estimator = trainer_lib.create_estimator(
      FLAGS.model,
      hp,
      t2t_trainer.create_run_config(hp),
      decode_hparams=decode_hp,
      use_tpu=FLAGS.use_tpu)

  output_decode = my_decode(estimator, hp, decode_hp,input_str)
  print('output-decode-res  = %s ' % str(output_decode))

if __name__ == "__main__":
  input_str='hello world'
  argv=['xxx.py',
        '--data_dir=/home/yechen/t2t_data',
        '--problem=translate_enzh_wmt32k',
        '--model=transformer',
        '--hparams_set=transformer_base',
        '--output_dir=/home/yechen/t2t_train/translate_enzh_wmt32k/transformer-transformer_base/v3',
        '--decode_hparams=beam_size=4,alpha=0.9']
  entry(argv,input_str)