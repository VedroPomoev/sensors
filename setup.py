#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


def get_version():
    local_results = {}
    execfile('sensors/version.py', {}, local_results)
    return local_results['__version__']


if __name__ == '__main__':
    setup(
        name='sensors',
        version=get_version(),
        packages=find_packages(),
        package_data = {
            'sensors': [
                '*.yml',
                'conf/*'
            ],
        },
        install_requires=[
            'psutil',
            'pyyaml'
        ],
        scripts=[
            'scripts/sensors'
        ]
    )
