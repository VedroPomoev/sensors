# -*- coding: utf-8 -*-

import os.path
import sys
import yaml


def load_config(config_file=None):
    if not config_file:
        config_file = os.path.join(os.path.dirname(__file__), 'conf', 'sensors.yml')
    with open(config_file, 'r') as f:
        config = yaml.load(f)
    return config


def probe_import(probe_full_name):
    splitted_name = probe_full_name.split('.')
    module_name = '.'.join(splitted_name[:-1])
    probe_name = splitted_name[-1]
    __import__(module_name)
    probe = getattr(sys.modules[module_name], probe_name)
    return probe


def run_probes(probes):
    result = {}
    for p in probes:
        probe_method = probe_import(p)
        probe_result = probe_method()
        result[p] = probe_result
    return result
