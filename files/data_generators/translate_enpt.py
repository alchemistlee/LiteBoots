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
from tensor2tensor.data_generators import text_encoder
from tensor2tensor.data_generators import text_problems
from tensor2tensor.data_generators import translate
from tensor2tensor.utils import registry

# End-of-sentence marker.
EOS = text_encoder.EOS_ID

_ENPT_TRAIN_DATASETS = [
    [
        "https://s3.amazonaws.com/web-language-models/paracrawl/release1/enpt.tgz", #hubo data
        ("enpt/enpt.en",
         "enpt/enpt.pt")
    ],
]
_ENPT_TEST_DATASETS = [
    [
        "https://s3.amazonaws.com/web-language-models/paracrawl/release1/enpt.tgz", #hubo data
        ("enpt/enpt.en",
         "enpt/enpt.pt")
    ],
]


@registry.register_problem
class TranslateEnptWmt32k(translate.TranslateProblem):
  """En-pt translation trained on WMT corpus."""

  @property
  def additional_training_datasets(self):
    """Allow subclasses to add training datasets."""
    return []

  def source_data_files(self, dataset_split):
    train = dataset_split == problem.DatasetSplit.TRAIN
    train_datasets = _ENPT_TRAIN_DATASETS + self.additional_training_datasets
    return train_datasets if train else _ENPT_TEST_DATASETS

  def vocab_data_files(self):
    return _ENPT_TRAIN_DATASETS


@registry.register_problem
class TranslateEnptWmtClean32k(TranslateEnptWmt32k):
  """En-pt translation trained on WMT with further cleaning."""

  @property
  def use_vocab_from_other_problem(self):
    return TranslateEnptWmt32k()

  @property
  def datatypes_to_clean(self):
    return ["txt"]


@registry.register_problem
class TranslateEnptWmt32kPacked(TranslateEnptWmt32k):

  @property
  def packed_length(self):
    return 256

  @property
  def use_vocab_from_other_problem(self):
    return TranslateEnptWmt32k()


@registry.register_problem
class TranslateEnptWmt8k(TranslateEnptWmt32k):
  """Problem spec for WMT En-Es translation."""

  @property
  def approx_vocab_size(self):
    return 2**13  # 8192


@registry.register_problem
class TranslateEnptWmt8kPacked(TranslateEnptWmt8k):

  @property
  def packed_length(self):
    return 256

  @property
  def use_vocab_from_other_problem(self):
    return TranslateEnptWmt8k()


@registry.register_problem
class TranslateEnptWmtCharacters(TranslateEnptWmt8k):
  """Problem spec for WMT En-Es translation."""

  @property
  def vocab_type(self):
    return text_problems.VocabType.CHARACTER