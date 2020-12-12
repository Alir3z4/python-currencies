import unittest
import sys

from setuptools import setup, find_packages, Command


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
    license='GNU GPL 3',
    author='Alireza Savand',
    author_email='alireza.savand@gmail.com',
    url='https://github.com/Alir3z4/python-currencies',
    cmdclass={'test': RunTests},
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development"
    ],
    python_requires='<4',
)
