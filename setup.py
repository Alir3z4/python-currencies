from setuptools import setup, find_packages

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
