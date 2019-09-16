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

"""Data generators for En-Et translation."""

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

# For English-Estonian the WMT18 data is used
# The complete corpus has ~ 2,18M sentences
_ENTR_TRAIN_DATASETS = [
    [
        "https://s3.amazonaws.com/web-language-models/paracrawl/release1/entr.tgz", #hubo data
        ("entr/entr.tr",
         "entr/entr.en")
    ],
]

# For development 2,000 parallel sentences are used
_ENTR_TEST_DATASETS = [
    [
        "https://s3.amazonaws.com/web-language-models/paracrawl/release1/entr.tgz", #hubo data
        ("entr/entr.tr",
         "entr/entr.en")
    ],
]


@registry.register_problem
class TranslateTrenWmt32k(translate.TranslateProblem):
  """Problem spec for WMT18 En-Et translation."""

  @property
  def approx_vocab_size(self):
    return 2**15  # 32768

  def source_data_files(self, dataset_split):
    train = dataset_split == problem.DatasetSplit.TRAIN
    return _ENTR_TRAIN_DATASETS if train else _ENTR_TEST_DATASETS


@registry.register_problem
class TranslateTrenWmtCharacters(translate.TranslateProblem):
  """Problem spec for WMT18 En-Et translation."""

  @property
  def vocab_type(self):
    return text_problems.VocabType.CHARACTER

  def source_data_files(self, dataset_split):
    train = dataset_split == problem.DatasetSplit.TRAIN
    return _ENTR_TRAIN_DATASETS if train else _ENTR_TEST_DATASETS