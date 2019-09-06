"""
This setup.py script is based on examples from  
https://pythonhosted.org/an_example_pypi_project/setuptools.html
https://docs.python.org/3/distutils/setupscript.
https://github.com/pypa/sampleproject/blob/master/setup.py
"""
from setuptools import setup, find_packages


from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np


with open('README', 'r') as fh: 
    long_description = fh.read()

# noinspection PyPackageRequirements
setup(
    name='fancy_means',
    version='0.1.0',
    packages=find_packages(),
    author='ASPP 2019',
    author_email='s.snape@hogwarts.ac.uk',
    description='an example python package',
    long_description=long_description,
    license='MIT',
    url='https://github.com/ASPP/2019-camerino-ODD.git',
    install_requires=['numpy >= 1.14.0',
                      'matplotlib >= 3.0.0',
                      'pytest >= 3.0.0'],
                      cmdclass = {'build_ext': build_ext},
    ext_modules = [
        Extension("fancy_means.fast_means", ["fancy_means/fast_means.pyx"],
              include_dirs=[np.get_include()],
              extra_compile_args=['-fopenmp'],
              extra_link_args=['-fopenmp', '-lgomp']),]
)
