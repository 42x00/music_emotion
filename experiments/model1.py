#!/usr/bin/env python
# encoding: utf-8

from jacinle.config.environ_v2 import configs, set_configs

from emotion.model.model import music_net

with set_configs():
    configs.train.weight_decay = 1e-5


def make_model(args):
    return music_net()
