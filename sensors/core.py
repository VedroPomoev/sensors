# -*- coding: utf-8 -*-

import os
import sys
import yaml


def load_config_file():
    """ Load configuration file in order (first found is used): ENV, HOME, /etc. """

    path_env = os.getenv('SENSORS_CONFIG', None)
    if path_env:
        path_env = os.path.expanduser(path_env)
    path_home = os.path.expanduser('~/.sensors.yml')
    path_etc = '/etc/sensors/sensors.yml'

    config = None
    for path in [path_env, path_home, path_etc]:
        if path and os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    config = yaml.load(f)
            except IOError as e:
                print("Error: {}".format(str(e)))
                sys.exit(1)
            except yaml.YAMLError as e:
                print("Error: {}".format(str(e)))
                sys.exit(1)
            return config

    print("Error: Configuration file not found.")
    sys.exit(1)


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
