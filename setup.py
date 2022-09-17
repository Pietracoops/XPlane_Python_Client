import os
from setuptools import setup, find_packages
import time

with open('README.md', encoding='utf-8') as f:
    long_desc = f.read()

setup(
    name='XPlaneApi',
    version='0.0.2',
    license='MIT',
    author="Massimo Pietracupa",
    author_email='Massimo.Pietracupa@hotmail.com',
    packages=['XPlaneApi', 'examples'],
    scripts=['examples/example1.py'],
    url='https://github.com/Pietracoops/XPlane_Python_Client',
    keywords='XPlane API',
    description='API Python Client for C++ Xplane Server',
    long_description_content_type='text/markdown',
    long_description=long_desc,
    install_requires=[
          'pyzmq==23.2.1',
          'zmq'
      ],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],

)