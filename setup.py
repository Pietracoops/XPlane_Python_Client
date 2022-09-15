from setuptools import setup, find_packages
import time

setup(
    name='XPlaneApi',
    version='0.0.1',
    license='MIT',
    author="Massimo Pietracupa",
    author_email='Massimo.Pietracupa@hotmail.com',
    packages=['XPlaneApi', 'examples'],
    scripts=['examples/example1.py'],
    url='https://github.com/Pietracoops/XPlane_Python_Client',
    keywords='XPlane API',
    description='API Python Client for C++ Xplane Server',
    long_description=open('README.rst').read(),
    install_requires=[
          'pyzmq==23.2.1',
          'zmq'
      ],

)