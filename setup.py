#! /usr/bin/env python2

from setuptools import setup

setup(name='deptree',
      version='1.0',
      description='Simple reverse depdency tree library',
      author='Matthew Parrott',
      author_email='matthewatabet@gmail.com',
      packages=['deptree'],
      package_dir={'': 'lib'},
      install_requires=['mock==1.3'],
      scripts=['bin/deptree'])
