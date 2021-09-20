# -*- coding: utf-8 -*-

"""
@date: 2021/7/20 下午10:20
@file: resnet.py
@author: zj
@description: 
"""

import torch

import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor
import torchvision.models as models

from zcls.config.key_word import KEY_OUTPUT

from .custom_basicblock import CustomBasicBlock
from .custom_bottlneck import CustomBottleneck
from ofd.config.key_word import KEY_FEAT


class ResNet(nn.Module):

    def __init__(self, num_classes=1000, arch='resnet50'):
        super().__init__()

        assert arch in ['resnet18', 'resnet34', 'resnet50', 'resnet101',
                        'resnet152', 'resnext50_32x4d', 'resnext101_32x8d']
        self.model = eval(f'models.{arch}')(pretrained=True)

        block = CustomBasicBlock if arch in ['resnet18', 'resnet34'] else CustomBottleneck
        self.model.layer1[-1] = block(self.model.layer1[-1])
        self.model.layer2[-1] = block(self.model.layer2[-1])
        self.model.layer3[-1] = block(self.model.layer3[-1])
        self.model.layer4[-1] = block(self.model.layer4[-1])

        self.init_weight(num_classes)

    def init_weight(self, num_classes):
        if num_classes != 1000:
            old_fc = self.model.fc
            assert isinstance(old_fc, nn.Linear)

            in_features = old_fc.in_features
            new_fc = nn.Linear(in_features, num_classes, bias=True)
            nn.init.normal_(new_fc.weight, 0, 0.01)
            nn.init.zeros_(new_fc.bias)

            self.model.fc = new_fc

    def _forward_impl(self, x: Tensor):
        # See note [TorchScript super()]
        x = self.model.conv1(x)
        x = self.model.bn1(x)
        x = self.model.relu(x)
        x = self.model.maxpool(x)

        feat1 = self.model.layer1(x)
        x = F.relu(feat1)
        feat2 = self.model.layer2(x)
        x = F.relu(feat2)
        feat3 = self.model.layer3(x)
        x = F.relu(feat3)
        feat4 = self.model.layer4(x)
        x = F.relu(feat4)

        x = self.model.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.model.fc(x)

        return x, [feat1, feat2, feat3, feat4]

    def forward(self, x):
        res, feat_list = self._forward_impl(x)

        return {
            KEY_OUTPUT: res,
            KEY_FEAT: feat_list
        }

    def get_distill_channels(self):
        channel1 = self.model.layer1[-1].bn3.num_features
        channel2 = self.model.layer2[-1].bn3.num_features
        channel3 = self.model.layer3[-1].bn3.num_features
        channel4 = self.model.layer4[-1].bn3.num_features

        return [channel1, channel2, channel3, channel4]

    def get_bn_before_relu(self):
        bn1 = self.model.layer1[-1].bn3
        bn2 = self.model.layer2[-1].bn3
        bn3 = self.model.layer3[-1].bn3
        bn4 = self.model.layer4[-1].bn3

        return [bn1, bn2, bn3, bn4]


def get_resnet(num_classes=1000, arch='resnet50'):
    return ResNet(num_classes=num_classes, arch=arch)


if __name__ == '__main__':
    model = get_resnet()
    print(model.get_distill_channels())

    data = torch.randn(1, 3, 224, 224)
    res_dict = model(data)
    for feats in res_dict[KEY_FEAT]:
        print(feats.shape)
