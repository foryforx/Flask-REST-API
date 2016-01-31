# -*- coding: utf-8 -*-
from setuptools import setup
import versioneer

setup(
    name='helloworld',
    packages=['helloworld'],
    zip_safe=False,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass()
)
