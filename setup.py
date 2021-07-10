# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in special_item_accountancy_code/__init__.py
from special_item_accountancy_code import __version__ as version

setup(
	name='special_item_accountancy_code',
	version=version,
	description='Change les code compteable article en fonction du parametrage client',
	author='scopen.fr',
	author_email='florian.henry@scopen.fr',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
