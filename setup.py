from setuptools import setup, find_packages


setup(
    name='XPlaneApi',
    version='0.0.1',
    license='MIT',
    author="Massimo Pietracupa",
    author_email='Massimo.Pietracupa@hotmail.com',
    packages=find_packages('XPlane_Api'),
    package_dir={'': 'XPlaneApi'},
    url='https://github.com/Pietracoops/XPlane_Python_Client',
    keywords='example project',
    install_requires=[
          'pyzmq==23.2.1',
          'zmq'
      ],

)