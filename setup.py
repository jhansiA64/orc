from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in orc/__init__.py
from orc import __version__ as version

setup(
	name="orc",
	version=version,
	description="ORC",
	author="Aravind Mandala",
	author_email="aravind.m@64network.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)