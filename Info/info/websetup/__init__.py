# -*- coding: utf-8 -*-
"""Setup the Info application"""

import logging

from info.config.app_cfg import base_config

__all__ = ['setup_app']

log = logging.getLogger(__name__)

from .schema import setup_schema
from .bootstrap import bootstrap


def setup_app(command, conf, vars):
    """Place any commands to setup info here"""
    conf = base_config.configure(conf.global_conf, conf.local_conf)
    base_config.setup(conf)

    setup_schema(command, conf, vars)
    bootstrap(command, conf, vars)
