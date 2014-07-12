import unittest
from setuptools import setup, find_packages, Command
import sys


class RunTests(Command):
    description = "run all tests for python-currencies"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        tests = unittest.TestLoader().discover('.')
        runner = unittest.TextTestRunner()
        results = runner.run(tests)
        sys.exit(not results.wasSuccessful())

setup(
    name='currencies',
    version=__import__("currencies").get_version(),
    description='Display money format and its filthy currencies, '
                'for all money lovers out there.',
    long_description=open('README.rst').read(),
    license=open('LICENSE').read(),
    author='Alireza Savand',
    author_email='alireza.savand@gmail.com',
    url='https://github.com/Alir3z4/python-currencies',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
