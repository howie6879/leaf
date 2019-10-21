#!/usr/bin/env python
"""
 Created by howie.hu at 2019-10-21.
"""

from setuptools import find_packages, setup

setup(
    name='leaf-cli',
    version='0.0.1',
    description="A CLI tool for hiding the application's icon in the Dock. (MacOS Dock栏软件图标隐藏终端工具)",
    install_requires=['fire'],
    author='Howie Hu',
    author_email='xiaozizayang@gmail.com',
    url="https://github.com/howie6879/leaf",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'leaf = leaf.cli:execute'
        ]
    },
)
