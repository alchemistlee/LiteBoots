# coding=utf-8
# Copyright 2019 The Tensor2Tensor Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Data generators for translation data-sets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensor2tensor.data_generators import problem
from tensor2tensor.data_generators import text_problems
from tensor2tensor.data_generators import translate
from tensor2tensor.data_generators import wiki_lm
from tensor2tensor.utils import registry


_ENDE_TRAIN_DATASETS = [
    [
        "http://data.statmt.org/wmt18/translation-task/training-parallel-nc-v13.tgz",  # pylint: disable=line-too-long
        ("training-parallel-nc-v13/news-commentary-v13.de-en.de",
         "training-parallel-nc-v13/news-commentary-v13.de-en.en")
    ],
    [
        "http://www.statmt.org/wmt13/training-parallel-commoncrawl.tgz",
        ("commoncrawl.de-en.de", "commoncrawl.de-en.en")
    ],
    [
        "http://www.statmt.org/wmt13/training-parallel-europarl-v7.tgz",
        ("training/europarl-v7.de-en.de", "training/europarl-v7.de-en.en")
    ],
    [
        "https://s3.amazonaws.com/web-language-models/paracrawl/release1/ende.tgz", #hubo data
        ("ende/ende.de",
         "ende/ende.en")
    ],
]

_ENDE_EVAL_DATASETS = [
    [
        "http://data.statmt.org/wmt17/translation-task/dev.tgz",
        ("dev/newstest2013.de", "dev/newstest2013.en")
    ],
]

_ENDE_RAPID_TRAIN_DATASET = [
    # additional training data available for WMT 18 news task training data
    # as defined by http://www.statmt.org/wmt18/translation-task.html
    [
        "http://data.statmt.org/wmt18/translation-task/rapid2016.tgz",
        ("rapid2016.de-en.de", "rapid2016.de-en.en"),
    ],
]

_ENDE_PARACRAWL_DATASETS = [
    [
        "https://s3.amazonaws.com/web-language-models/paracrawl/release4/en-de.bicleaner07.tmx.gz",  # pylint: disable=line-too-long
        ("tmx", "en-de.bicleaner07.tmx.gz")
    ]
]


@registry.register_problem
class TranslateDeenWmt32k(translate.TranslateProblem):
  """En-de translation trained on WMT corpus."""

  @property
  def additional_training_datasets(self):
    """Allow subclasses to add training datasets."""
    #return []
    return _ENDE_RAPID_TRAIN_DATASET

  def source_data_files(self, dataset_split):
    train = dataset_split == problem.DatasetSplit.TRAIN
    train_datasets = _ENDE_TRAIN_DATASETS + self.additional_training_datasets
    return train_datasets if train else _ENDE_EVAL_DATASETS


@registry.register_problem
class TranslateDeen2018Wmt32k(translate.TranslateProblem):
  """En-de translation trained on WMT18 corpus."""

  @property
  def use_vocab_from_other_problem(self):
    return TranslateDeenWmt32k()

  @property
  def additional_training_datasets(self):
    """WMT18 adds rapid data."""
    return _ENDE_RAPID_TRAIN_DATASET


@registry.register_problem
class TranslateDeenWmtClean32k(TranslateDeenWmt32k):
  """En-de translation trained on WMT with further cleaning."""

  @property
  def use_vocab_from_other_problem(self):
    return TranslateDeenWmt32k()

  @property
  def datatypes_to_clean(self):
    return ["txt"]


@registry.register_problem
class TranslateDeenPc32k(translate.TranslateProblem):
  """En-de translation trained on Paracrawl (bicleaner corpus)."""

  @property
  def use_vocab_from_other_problem(self):
    return TranslateDeenWmt32k()

  @property
  def additional_training_datasets(self):
    """Allow subclasses to add training datasets."""
    return []

  def source_data_files(self, dataset_split):
    train = dataset_split == problem.DatasetSplit.TRAIN
    train_datasets = (
        _ENDE_PARACRAWL_DATASETS + self.additional_training_datasets)
    return train_datasets if train else _ENDE_EVAL_DATASETS


@registry.register_problem
class TranslateDeenPcClean32k(TranslateDeenPc32k):
  """En-de translation trained on Paracrawl with further cleaning."""

  @property
  def datatypes_to_clean(self):
    return ["tmx"]


@registry.register_problem
class TranslateDeenWmtPc32k(TranslateDeenWmt32k):
  """En-de translation trained on WMT plus Paracrawl."""

  @property
  def use_vocab_from_other_problem(self):
    return TranslateDeenWmt32k()

  @property
  def additional_training_datasets(self):
    return _ENDE_PARACRAWL_DATASETS


@registry.register_problem
class TranslateDeenWmtCleanPc32k(TranslateDeenWmtPc32k):
  """En-de translation trained on cleaned WMT plus Paracrawl."""

  @property
  def datatypes_to_clean(self):
    return ["txt"]


@registry.register_problem
class TranslateDeenWmtPcClean32k(TranslateDeenWmtPc32k):
  """En-de translation trained on WMT plus cleaned Paracrawl."""

  @property
  def datatypes_to_clean(self):
    return ["tmx"]


@registry.register_problem
class TranslateDeenWmtCleanPcClean32k(TranslateDeenWmtPcClean32k):
  """En-de translation trained on cleaned WMT plus cleaned Paracrawl."""

  @property
  def datatypes_to_clean(self):
    return ["txt", "tmx"]


@registry.register_problem
class TranslateDeenWmt32kPacked(TranslateDeenWmt32k):

  @property
  def packed_length(self):
    return 256

  @property
  def use_vocab_from_other_problem(self):
    return TranslateDeenWmt32k()


@registry.register_problem
class TranslateDeenWmt8k(TranslateDeenWmt32k):
  """Problem spec for WMT En-De translation."""

  @property
  def approx_vocab_size(self):
    return 2**13  # 8192


@registry.register_problem
class TranslateDeenWmt8kPacked(TranslateDeenWmt8k):

  @property
  def packed_length(self):
    return 256

  @property
  def use_vocab_from_other_problem(self):
    return TranslateDeenWmt8k()


@registry.register_problem
class TranslateDeenWmtCharacters(TranslateDeenWmt8k):
  """Problem spec for WMT En-De translation."""

  @property
  def vocab_type(self):
    return text_problems.VocabType.CHARACTER


@registry.register_problem
class TranslateDeenWmtMulti64k(TranslateDeenWmt8k):
  """Translation with muli-lingual vocabulary."""

  @property
  def use_vocab_from_other_problem(self):
    return wiki_lm.LanguagemodelEndeFrRoWiki64k()


@registry.register_problem
class TranslateDeenWmtMulti64kPacked1k(TranslateDeenWmtMulti64k):
  """Translation with muli-lingual vocabulary."""

  @property
  def packed_length(self):
    return 1024

  @property
  def num_training_examples(self):
    return 173800

  @property
  def inputs_prefix(self):
    return "translate English German "

  @property
  def targets_prefix(self):
    return "translate German English "