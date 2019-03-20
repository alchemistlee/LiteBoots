# coding = utf-8

# @time    : 2019/3/19 3:35 PM
# @author  : alchemistlee
# @fileName: liteboots_server.py
# @abstract:

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from tensor2tensor.bin import t2t_trainer
from tensor2tensor.data_generators import text_encoder
# from tensor2tensor.utils import decoding
from tensor2tensor.utils import registry
from tensor2tensor.utils import trainer_lib
from tensor2tensor.utils import usr_dir
# import my_trainer_lib

import collections
import operator
import time

import numpy as np
import six
from six.moves import input  # pylint: disable=redefined-builtin

from tensor2tensor.data_generators import problem as problem_lib
from tensor2tensor.data_generators import text_problems

import my_decoding

import tensorflow as tf

import sys
import json

import threading
from queue import Queue
from connect import ConnectManager
import config
import hashlib
from multiprocessing import freeze_support
import fire



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

self_defined_hp=['xxx.py',
        '--data_dir=/home/yechen/t2t_data',
        '--problem=translate_enzh_wmt32k',
        '--model=transformer',
        '--hparams_set=transformer_base',
        '--output_dir=/home/yechen/t2t_train/translate_enzh_wmt32k/transformer-transformer_base/v3',
        '--decode_hparams=beam_size=4,alpha=0.9']

flags.FLAGS(self_defined_hp, known_only=True)

IMAGE_DECODE_LENGTH = 100


class LiteBootsServer(object):

  def __init__(self,host, port, authkey):
    self._host = host
    self._port = port
    self._address = '%s:%s' % (self._host, self._port)
    self._authkey = str(authkey).encode('utf-8')
    self._task_queue = Queue()
    self._task_result = dict()
    self._manager = ConnectManager(address=(self._host, self._port), authkey=self._authkey)
    self._initialize()

  def _initialize(self):
    ConnectManager.register(config.REMOTE_PUSH_FUNC, callable=self.push)
    ConnectManager.register(config.REMOTE_RESULT_FUNC, callable=self.result)
    ConnectManager.register(config.REMOTE_PREDICT_FUNC, callable=self.predict)
    threading.Thread(target=self._manager.server).start()
    print('host: %s start success!' % self._address)

  def push(self,  content):
    md5=self.md5(content)
    print('uid: %s, string: %s' % (md5, content))
    self._task_queue.put((md5, content))

  def create_hparams(self):
    print('xx create_hparams')
    return trainer_lib.create_hparams(
      FLAGS.hparams_set,
      FLAGS.hparams,
      data_dir=os.path.expanduser(FLAGS.data_dir),
      problem_name=FLAGS.problem)

  def md5(self,str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    md5_str=m.hexdigest()
    return md5_str

  def create_decode_hparams(self):
    print('xx create_decode_hparams')
    decode_hp = my_decoding.decode_hparams(FLAGS.decode_hparams)
    decode_hp.shards = FLAGS.decode_shards
    decode_hp.shard_id = FLAGS.worker_id
    decode_hp.decode_in_memory = FLAGS.decode_in_memory
    decode_hp.decode_to_file = FLAGS.decode_to_file
    decode_hp.decode_reference = FLAGS.decode_reference
    return decode_hp


  def create_new_estimator(self,hp,decode_hp):
    estimator = trainer_lib.create_estimator(
      FLAGS.model,
      hp,
      t2t_trainer.create_run_config(hp),
      decode_hparams=decode_hp,
      use_tpu=FLAGS.use_tpu)
    return estimator


  def my_decode(self,estimator, hparams, decode_hp):
    return self.decode_my_data_v2(estimator, hparams, decode_hp,
                                  checkpoint_path=FLAGS.checkpoint_path)
  # def decode(self,estimator, hparams, decode_hp):
  #   """Decode from estimator. Interactive, from file, or from dataset."""
  #   if FLAGS.decode_interactive:
  #     if estimator.config.use_tpu:
  #       raise ValueError("TPU can only decode from dataset.")
  #     decoding.decode_interactively(estimator, hparams, decode_hp,
  #                                   checkpoint_path=FLAGS.checkpoint_path)
  #   elif FLAGS.decode_from_file:
  #     if estimator.config.use_tpu:
  #       raise ValueError("TPU can only decode from dataset.")
  #     decoding.decode_from_file(estimator, FLAGS.decode_from_file, hparams,
  #                               decode_hp, FLAGS.decode_to_file,
  #                               checkpoint_path=FLAGS.checkpoint_path)
  #     if FLAGS.checkpoint_path and FLAGS.keep_timestamp:
  #       ckpt_time = os.path.getmtime(FLAGS.checkpoint_path + ".index")
  #       os.utime(FLAGS.decode_to_file, (ckpt_time, ckpt_time))
  #   else:
  #     decoding.decode_from_dataset(
  #         estimator,
  #         FLAGS.problem,
  #         hparams,
  #         decode_hp,
  #         decode_to_file=FLAGS.decode_to_file,
  #         dataset_split="test" if FLAGS.eval_use_test_set else None)


# def score_file(filename):
  # """Score each line in a file and return the scores."""
  # # Prepare model.
  # hparams = create_hparams()
  # encoders = registry.problem(FLAGS.problem).feature_encoders(FLAGS.data_dir)
  # has_inputs = "inputs" in encoders
  #
  # # Prepare features for feeding into the model.
  # if has_inputs:
  #   inputs_ph = tf.placeholder(dtype=tf.int32)  # Just length dimension.
  #   batch_inputs = tf.reshape(inputs_ph, [1, -1, 1, 1])  # Make it 4D.
  # targets_ph = tf.placeholder(dtype=tf.int32)  # Just length dimension.
  # batch_targets = tf.reshape(targets_ph, [1, -1, 1, 1])  # Make it 4D.
  # features = {
  #     "inputs": batch_inputs,
  #     "targets": batch_targets,
  # } if has_inputs else {"targets": batch_targets}
  #
  # # Prepare the model and the graph when model runs on features.
  # model = registry.model(FLAGS.model)(hparams, tf.estimator.ModeKeys.EVAL)
  # _, losses = model(features)
  # saver = tf.train.Saver()
  #
  # with tf.Session() as sess:
  #   # Load weights from checkpoint.
  #   ckpts = tf.train.get_checkpoint_state(FLAGS.output_dir)
  #   ckpt = ckpts.model_checkpoint_path
  #   saver.restore(sess, ckpt)
  #   # Run on each line.
  #   with tf.gfile.Open(filename) as f:
  #     lines = f.readlines()
  #   results = []
  #   for line in lines:
  #     tab_split = line.split("\t")
  #     if len(tab_split) > 2:
  #       raise ValueError("Each line must have at most one tab separator.")
  #     if len(tab_split) == 1:
  #       targets = tab_split[0].strip()
  #     else:
  #       targets = tab_split[1].strip()
  #       inputs = tab_split[0].strip()
  #     # Run encoders and append EOS symbol.
  #     targets_numpy = encoders["targets"].encode(
  #         targets) + [text_encoder.EOS_ID]
  #     if has_inputs:
  #       inputs_numpy = encoders["inputs"].encode(inputs) + [text_encoder.EOS_ID]
  #     # Prepare the feed.
  #     feed = {
  #         inputs_ph: inputs_numpy,
  #         targets_ph: targets_numpy
  #     } if has_inputs else {targets_ph: targets_numpy}
  #     # Get the score.
  #     np_loss = sess.run(losses["training"], feed)
  #     results.append(np_loss)
  # return results

  def make_input_fn_from_generator(self,gen):
    """Use py_func to yield elements from the given generator."""
    first_ex = six.next(gen)
    flattened = tf.contrib.framework.nest.flatten(first_ex)
    types = [t.dtype for t in flattened]
    shapes = [[None] * len(t.shape) for t in flattened]
    first_ex_list = [first_ex]

    def py_func():
      if first_ex_list:
        example = first_ex_list.pop()
      else:
        example = six.next(gen)
      return tf.contrib.framework.nest.flatten(example)

    def input_fn():
      flat_example = tf.py_func(py_func, [], types)
      _ = [t.set_shape(shape) for t, shape in zip(flat_example, shapes)]
      example = tf.contrib.framework.nest.pack_sequence_as(first_ex, flat_example)
      return example

    return input_fn

  def _interactive_input_fn(self,hparams, decode_hp):
    """Generator that reads from the terminal and yields "interactive inputs".

    Due to temporary limitations in tf.learn, if we don't want to reload the
    whole graph, then we are stuck encoding all of the input as one fixed-size
    numpy array.

    We yield int32 arrays with shape [const_array_size].  The format is:
    [num_samples, decode_length, len(input ids), <input ids>, <padding>]

    Args:
      hparams: model hparams
      decode_hp: decode hparams
    Yields:
      numpy arrays

    Raises:
      Exception: when `input_type` is invalid.
    """
    num_samples = decode_hp.num_samples if decode_hp.num_samples > 0 else 1
    decode_length = decode_hp.extra_length
    # input_type = "text"
    p_hparams = hparams.problem_hparams
    has_input = "inputs" in p_hparams.input_modality
    vocabulary = p_hparams.vocabulary["inputs" if has_input else "targets"]
    # This should be longer than the longest input.
    const_array_size = 10000
    # Import readline if available for command line editing and recall.
    # try:
    #   import readline  # pylint: disable=g-import-not-at-top,unused-variable
    # except ImportError:
    #   pass
    while True:
      # prompt = ("INTERACTIVE MODE  num_samples=%d  decode_length=%d  \n"
      #           "  it=<input_type>     ('text' or 'image' or 'label', default: "
      #           "text)\n"
      #           "  ns=<num_samples>    (changes number of samples, default: 1)\n"
      #           "  dl=<decode_length>  (changes decode length, default: 100)\n"
      #           "  <%s>                (decode)\n"
      #           "  q                   (quit)\n"
      #           ">" % (num_samples, decode_length, "source_string"
      # if has_input else "target_prefix"))
      # input_string = input(prompt)
      # if input_string == "q":
      #   return
      # elif input_string[:3] == "ns=":
      #   num_samples = int(input_string[3:])
      # elif input_string[:3] == "dl=":
      #   decode_length = int(input_string[3:])
      # elif input_string[:3] == "it=":
      #   input_type = input_string[3:]
      # else:
      #   if input_type == "text":

      if(self._task_queue.empty()):
        continue
      uid, input_string = self._task_queue.get()

      input_ids = vocabulary.encode(input_string)
      if has_input:
        input_ids.append(text_encoder.EOS_ID)
      x = [num_samples, decode_length, len(input_ids)] + input_ids
      assert len(x) < const_array_size
      x += [0] * (const_array_size - len(x))
      features = {
        "inputs": np.array(x).astype(np.int32),
      }
        # elif input_type == "image":
        #   input_path = input_string
        #   img = vocabulary.encode(input_path)
        #   features = {
        #     "inputs": img.astype(np.int32),
        #   }
        # elif input_type == "label":
        #   input_ids = [int(input_string)]
        #   x = [num_samples, decode_length, len(input_ids)] + input_ids
        #   features = {
        #     "inputs": np.array(x).astype(np.int32),
        #   }
        # else:
        #   raise Exception("Unsupported input type.")
      for k, v in six.iteritems(
          problem_lib.problem_hparams_to_features(p_hparams)):
        features[k] = np.array(v).astype(np.int32)
      yield features

  def _interactive_input_tensor_to_features_dict(self,feature_map, hparams):
    """Convert the interactive input format (see above) to a dictionary.

    Args:
      feature_map: dict with inputs.
      hparams: model hyperparameters

    Returns:
      a features dictionary, as expected by the decoder.
    """
    inputs = tf.convert_to_tensor(feature_map["inputs"])
    input_is_image = False if len(inputs.get_shape()) < 3 else True

    x = inputs
    if input_is_image:
      x = tf.image.resize_images(x, [299, 299])
      x = tf.reshape(x, [1, 299, 299, -1])
      x = tf.to_int32(x)
    else:
      # Remove the batch dimension.
      num_samples = x[0]
      length = x[2]
      x = tf.slice(x, [3], tf.to_int32([length]))
      x = tf.reshape(x, [1, -1, 1, 1])
      # Transform into a batch of size num_samples to get that many random
      # decodes.
      x = tf.tile(x, tf.to_int32([num_samples, 1, 1, 1]))

    p_hparams = hparams.problem_hparams
    input_space_id = tf.constant(p_hparams.input_space_id)
    target_space_id = tf.constant(p_hparams.target_space_id)

    features = {}
    features["input_space_id"] = input_space_id
    features["target_space_id"] = target_space_id
    features["decode_length"] = (
      IMAGE_DECODE_LENGTH if input_is_image else inputs[1])
    features["inputs"] = x
    return features

  def _save_until_eos(self,ids, skip=False):
    """Strips everything after the first <EOS> token, which is normally 1."""
    ids = ids.flatten()
    if skip:
      return ids
    try:
      index = list(ids).index(text_encoder.EOS_ID)
      return ids[0:index]
    except ValueError:
      # No EOS_ID: return the array as-is.
      return ids

  def log_decode_results(self,
                        inputs,
                        outputs,
                        problem_name,
                        prediction_idx,
                        inputs_vocab,
                        targets_vocab,
                        targets=None,
                        save_images=False,
                        output_dir=None,
                        identity_output=False,
                        log_results=True):
    """Log inference results."""

    # TODO(lukaszkaiser) refactor this into feature_encoder
    # is_video = "video" in problem_name or "gym" in problem_name
    # if is_video:
    #   def fix_and_save_video(vid, prefix):
    #     save_path_template = os.path.join(
    #         output_dir,
    #         "%s_%s_%05d_{:05d}.png" % (problem_name, prefix, prediction_idx))
    #     # this is only required for predictions
    #     if vid.shape[-1] == 1:
    #       vid = np.squeeze(vid, axis=-1)
    #     save_video(vid, save_path_template)
    #   tf.logging.info("Saving video: {}".format(prediction_idx))
    #   fix_and_save_video(inputs, "inputs")
    #   fix_and_save_video(outputs, "outputs")
    #   fix_and_save_video(targets, "targets")

    is_image = "image" in problem_name
    is_text2class = isinstance(registry.problem(problem_name),
                               text_problems.Text2ClassProblem)
    skip_eos_postprocess = is_image or is_text2class

    decoded_inputs = None
    # if is_image and save_images:
    #   save_path = os.path.join(
    #       output_dir, "%s_prediction_%d.jpg" % (problem_name, prediction_idx))
    #   show_and_save_image(inputs / 255., save_path)

    if inputs_vocab:
      if identity_output:
        decoded_inputs = " ".join(map(str, inputs.flatten()))
      else:
        decoded_inputs = inputs_vocab.decode(self._save_until_eos(
            inputs, skip_eos_postprocess))

      if log_results :
        tf.logging.info("Inference results INPUT: %s" % decoded_inputs)

    decoded_targets = None
    decoded_outputs = None
    if identity_output:
      decoded_outputs = " ".join(map(str, outputs.flatten()))
      if targets is not None:
        decoded_targets = " ".join(map(str, targets.flatten()))
    else:
      decoded_outputs = targets_vocab.decode(self._save_until_eos(
          outputs, skip_eos_postprocess))
      if targets is not None and log_results:
        decoded_targets = targets_vocab.decode(self._save_until_eos(
            targets, skip_eos_postprocess))


    tf.logging.info("Inference results OUTPUT: %s" % decoded_outputs)

    if targets is not None and log_results:
      tf.logging.info("Inference results TARGET: %s" % decoded_targets)

    return decoded_inputs, decoded_outputs, decoded_targets



  def decode_my_data_v2(self, estimator, hparams, decode_hp, checkpoint_path=None):

    is_image = "image" in hparams.problem.name
    is_text2class = isinstance(hparams.problem,
                               text_problems.Text2ClassProblem)
    skip_eos_postprocess = is_image or is_text2class

    p_hp = hparams.problem_hparams
    has_input = "inputs" in p_hp.vocabulary
    inputs_vocab_key = "inputs" if has_input else "targets"
    inputs_vocab = p_hp.vocabulary[inputs_vocab_key]
    targets_vocab = p_hp.vocabulary["targets"]
    problem_name = FLAGS.problem

    def input_fn():
      gen_fn = self.make_input_fn_from_generator(
        self._interactive_input_fn(hparams, decode_hp))
      example = gen_fn()
      example = self._interactive_input_tensor_to_features_dict(example, hparams)
      return example

    result_iter = estimator.predict(input_fn, checkpoint_path=checkpoint_path)
    for result in result_iter:
      # targets_vocab = hparams.problem_hparams.vocabulary["targets"]
      # if decode_hp.return_beams:
      #   beams = np.split(result["outputs"], decode_hp.beam_size, axis=0)
      #   scores = None
      #   if "scores" in result:
      #     scores = np.split(result["scores"], decode_hp.beam_size, axis=0)
      #   for k, beam in enumerate(beams):
      #     tf.logging.info("BEAM %d:" % k)
      #     beam_string = targets_vocab.decode(self._save_until_eos(
      #       beam, skip_eos_postprocess))
      #     if scores is not None:
      #       tf.logging.info("\"%s\"\tScore:%f" % (beam_string, scores[k]))
      #     else:
      #       tf.logging.info("\"%s\"" % beam_string)
      # else:
      #   if decode_hp.identity_output:
      #     tf.logging.info(" ".join(map(str, result["outputs"].flatten())))
      #   else:
      # tf.logging.info(
      #   targets_vocab.decode(self._save_until_eos(
      #     result["outputs"], skip_eos_postprocess)))
      decoded_inputs , decoded_outputs, _ = self.log_decode_results(
        result["inputs"],
        result["outputs"],
        problem_name,
        None,
        inputs_vocab,
        targets_vocab,
        log_results=decode_hp.log_results)
      print('decode-input = %s ' % str(decoded_inputs))
      print('decode-output = %s ' % str(decoded_outputs))
      input_md5=self.md5(decoded_inputs)
      self._task_result[input+input_md5]=decoded_outputs

  def entry(self):
    # global estimator
    # global hp
    # global decode_hp
    # flags.FLAGS(argv , known_only=True)

    tf.logging.set_verbosity(tf.logging.INFO)
    trainer_lib.set_random_seed(FLAGS.random_seed)
    usr_dir.import_usr_dir(FLAGS.t2t_usr_dir)

    print("###self defined hp###")
    print(str(FLAGS.data_dir))
    print(str(FLAGS.problem))
    print(str(FLAGS.model))
    print(str(FLAGS.hparams_set))
    print(str(FLAGS.output_dir))
    print(str(FLAGS.decode_hparams))

    # if hp is None:
    #   print('hp is None !')
    #   hp = create_hparams()
    # if decode_hp is None:
    #   print('decode_hp is None !')
    #   decode_hp = create_decode_hparams()
    # if estimator is None:
    #   print('estimator is None !')
    #   estimator = my_trainer_lib.create_estimator(
    #     FLAGS.model,
    #     hp,
    #     t2t_trainer.create_run_config(hp),
    #     decode_hparams=decode_hp,
    #     use_tpu=FLAGS.use_tpu)

    hp = self.create_hparams()
    decode_hp = self.create_decode_hparams()
    estimator = self.create_new_estimator(hp, decode_hp)

    output_decode = self.my_decode(estimator, hp, decode_hp)
    print('output decode-res  = %s ' % str(output_decode))
    return output_decode


  # def test_entry():
  #   global self_defined_hp
  #   input_str = 'hello world'
  #   entry(self_defined_hp, input_str)

def main(host, port, authkey=None):
  LiteBootsServer(host, port, authkey).entry()

# @app.route("/translate/en2zh/",methods=['GET'])
# def trans_en2zh():
#   global self_defined_hp
#   input_str = request.args.get('in')
#   print('input-str = %s ' % input_str)
#   decode_res =entry(input_str)
#   # print('output = %s ' % str(decode_res))
#   res={
#       'res':str(decode_res)
#   }
#   return json.dumps(res)


if __name__ == "__main__":
  freeze_support()
  fire.Fire(main)
