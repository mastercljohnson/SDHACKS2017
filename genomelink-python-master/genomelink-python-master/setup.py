import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='genomelink',
    version='0.1.4',
    description='GENOMELINK',
    long_description='',
    author='AWAKENS',
    author_email='',
    url='https://github.com/awakens-dev/genomelink-python',
    packages=['genomelink', 'genomelink.resource'],
    install_requires=[
        'requests',
        'requests_oauthlib'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
        # 'Programming Language :: Python :: 3.6',
        # 'Programming Language :: Python :: Implementation :: PyPy'
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ])
