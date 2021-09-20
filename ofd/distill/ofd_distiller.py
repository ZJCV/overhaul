# -*- coding: utf-8 -*-

"""
@date: 2021/8/29 下午1:11
@file: ofd_distiller.py
@author: zj
@description: 
"""

import math
import torch

import torch.nn as nn
from scipy.stats import norm
from zcls.model.init_helper import init_weights
from zcls.config.key_word import KEY_OUTPUT

from ofd.config.key_word import KEY_FEAT, KEY_T_FEAT, KEY_S_FEAT


def create_student_transform(t_channel, s_channel):
    return nn.Sequential(
        nn.Conv2d(s_channel, t_channel, kernel_size=(1, 1)),
        nn.BatchNorm2d(t_channel)
    )


def get_margin_from_BN(bn):
    assert isinstance(bn, nn.BatchNorm2d)
    margin = list()
    std = bn.weight.data
    mean = bn.bias.data
    for (s, m) in zip(std, mean):
        s = abs(s.item())
        m = m.item()
        if norm.cdf(-m / s) > 0.001:
            margin.append(- s * math.exp(- (m / s) ** 2 / 2) / math.sqrt(2 * math.pi) / norm.cdf(-m / s) + m)
        else:
            margin.append(-3 * s)

    return torch.FloatTensor(margin).to(std.device)


def teacher_transform(x, margin):
    return torch.max(x, margin)


class OFDDistiller(nn.Module):

    def __init__(self, t_net, s_net):
        super().__init__()
        assert isinstance(t_net, torch.nn.Module)
        assert isinstance(s_net, torch.nn.Module)
        assert len(t_net.get_distill_channels()) == len(s_net.get_distill_channels())

        s_transform_list = list()
        for t_channel, s_channel in zip(t_net.get_distill_channels(), s_net.get_distill_channels()):
            s_transform_list.append(create_student_transform(t_channel, s_channel))

        margin_list = list()
        for t_bn in t_net.get_bn_before_relu():
            margin = get_margin_from_BN(t_bn)
            margin_list.append(margin)
        assert len(margin_list) == len(s_transform_list)

        self.t_net = t_net
        self.t_net.train()
        # freeze grad update but keep train state
        self.t_net.requires_grad_(False)

        self.s_net = s_net
        self.s_net.train()

        self.s_transform_list = nn.ModuleList(s_transform_list)
        for i, margin in enumerate(margin_list):
            self.register_buffer('margin%d' % (i + 1), margin.unsqueeze(1).unsqueeze(2).unsqueeze(0).detach())

        self.__init_weights__()

    def __init_weights__(self):
        for student_transform in self.s_transform_list:
            init_weights(student_transform)

    def forward(self, x):
        t_outputs_dict = self.t_net(x)
        s_outputs_dict = self.s_net(x)

        t_transform_feat_list = list()
        for i, t_feat in enumerate(t_outputs_dict[KEY_FEAT]):
            t_transform_feat_list.append(teacher_transform(t_feat, getattr(self, 'margin%d' % (i + 1))))

        s_transform_feat_list = list()
        for s_feat, s_transform in zip(s_outputs_dict[KEY_FEAT], self.s_transform_list):
            s_transform_feat_list.append(s_transform(s_feat))

        return {
            KEY_OUTPUT: s_outputs_dict[KEY_OUTPUT],
            KEY_T_FEAT: t_transform_feat_list,
            KEY_S_FEAT: s_transform_feat_list
        }
