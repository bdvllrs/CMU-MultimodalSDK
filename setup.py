from setuptools import find_packages, setup

setup(name='mmsdk',
      version='1.1.1',
      install_requires=['h5py', 'validators', 'tqdm', 'numpy', 'argparse', 'requests'],
      packages=find_packages())