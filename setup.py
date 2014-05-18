from setuptools import setup

import pyr3

setup(
    name='pyr3',
    version='0.1.0',
    author='Omer Katz',
    email='omer.drow@gmail.com',
    zip_safe=False,
    ext_package='pyr3',
    ext_modules=[pyr3.ffi.verifier.get_extension()],
)
