# -*- coding: utf-8 -*-

"""
@date: 2021/9/7 下午7:55
@file: mobilenet.py
@author: zj
@description: 
"""

import torch
import torchvision.models
from torchvision.models.mobilenetv2 import InvertedResidual, ConvBNActivation

from ofd.model.mobilenet.mobilenet_v2 import get_mobilenet_v2
from zcls.config.key_word import KEY_OUTPUT
from ofd.config.key_word import KEY_FEAT

if __name__ == '__main__':
    model = get_mobilenet_v2()

    data = torch.randn(1, 3, 224, 224)
    res = model(data)

    feats_list = res[KEY_FEAT]
    outputs = res[KEY_OUTPUT]
    for feats in feats_list:
        print(feats.shape)
