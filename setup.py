import os

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

version = '0.0.1'


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(name='django-json-tag',
      version=version,
      author="fusionbox, inc.",
      author_email="programmers@fusionbox.com",
      maintainer="Thomas Grainger",
      maintainer_email="django-json-tag@graingert.co.uk",
      url="https://github.com/graingert/django-json-tag",
      keywords="rest json views django helpers",
      description="A lightweight collection of JSON helpers for Django.",
      long_description=read_file('README.rst') + '\n\n' + read_file('CHANGELOG.rst'),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      install_requires=['Django>=1.8'],
      packages=find_packages(
          exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
      ),
)
