# -*- coding: utf-8 -*-

"""
@date: 2021/7/20 下午10:20
@file: mobilenet_v2.py
@author: zj
@description: 
"""

import torch.nn as nn
import torchvision.models as models

from zcls.config.key_word import KEY_OUTPUT


class MobileNetV2(nn.Module):

    def __init__(self, num_classes=1000, arch='mobilenet_v2'):
        super().__init__()

        assert arch in ['mobilenet_v2']
        self.model = eval(f'models.{arch}')(pretrained=True)

        self.init_weight(num_classes)

    def init_weight(self, num_classes):
        if num_classes != 1000:
            old_fc = self.model.classifier[1]
            assert isinstance(old_fc, nn.Linear)

            in_features = old_fc.in_features
            new_fc = nn.Linear(in_features, num_classes, bias=True)
            nn.init.normal_(new_fc.weight, 0, 0.01)
            nn.init.zeros_(new_fc.bias)

            self.model.classifier[1] = new_fc

    def forward(self, x):
        res = self.model(x)

        return {KEY_OUTPUT: res}


def get_mobilenet_v2(num_classes=1000, arch='mobilenet_v2'):
    return MobileNetV2(num_classes=num_classes, arch=arch)
