#! /usr/bin/env python2

from distutils.core import setup

setup(name='Dependency Tree',
      version='1.0',
      description='Simple reverse depdency tree library',
      author='Matthew Parrott',
      author_email='matthewatabet@gmail.com',
      packages=['deptree'],
      scripts=['bin/deptree'])
