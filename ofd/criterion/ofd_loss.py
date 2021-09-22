# -*- coding: utf-8 -*-

"""
@date: 2021/8/29 上午11:56
@file: ofd_loss.py
@author: zj
@description: 
"""

import torch

from abc import ABC
import torch.nn as nn
from zcls.config.key_word import KEY_OUTPUT, KEY_LOSS
from zcls.model import registry

from ofd.config.key_word import KEY_T_FEAT, KEY_S_FEAT, KEY_TASK_LOSS, KEY_DISTILL_LOSS


@registry.CRITERION.register('OFDLoss')
class OFDLoss(nn.Module, ABC):

    def __init__(self, cfg):
        super(OFDLoss, self).__init__()
        self.task_loss = nn.CrossEntropyLoss(reduction='mean')
        self.distill_loss = nn.MSELoss(reduction='none')
        self.lam = cfg.DISTILL.LAMBDA

    def __call__(self, output_dict, targets):
        assert isinstance(output_dict, dict) and KEY_OUTPUT in output_dict.keys()
        inputs = output_dict[KEY_OUTPUT]
        task_loss = self.task_loss(inputs, targets)

        t_feat_list = output_dict[KEY_T_FEAT]
        s_feat_list = output_dict[KEY_S_FEAT]
        assert len(t_feat_list) == len(s_feat_list)

        distill_loss = 0
        for i, (t_feat, s_feat) in enumerate(zip(t_feat_list, s_feat_list)):
            tmp_loss = self.distill_loss(s_feat, t_feat)

            mask = ((s_feat > t_feat) | (t_feat > 0)).float()
            tmp_loss = tmp_loss * mask
            distill_loss += torch.sum(tmp_loss) / torch.sum(mask)
        distill_loss = distill_loss * self.lam

        return {
            KEY_TASK_LOSS: task_loss,
            KEY_DISTILL_LOSS: distill_loss,
            KEY_LOSS: task_loss + distill_loss,
        }
