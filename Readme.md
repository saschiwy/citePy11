# C++ Interface Translation Engine for Pybind11 (CitePy11)

## Introduction

The engine intends to create pybind11 bindings out of a CPP Interface Header and also if desired a python mapper to add
support for IDE development

## Features
- Create pybind11 bindings out of a CPP Interface Header
- Create a python mapper to add support for IDE development and easy to use
- Adds doxygen comments to the python bindings as docstrings
- Overloading support
- Operator overloading support
- Namespace support
- Custom method support
- Custom method ignore support

## Required Software

- CMake >= 3.14
- A CMake compatible compiler
- python >= 3.7
- [pybind11](https://github.com/pybind/pybind11) is added by CMake automatically

~~~~
pip install -r requirements.txt
~~~~ 

## Getting started:

- Create the binding ([binding example](./create_example_binding.py))
    - Create the config with the desired headers
    - Add or ignore custom methods for python wrappers
    - Create the binding (with optional python Mapper)
- Compile the C++ library ([CMake example](citePyExample/CMakeLists.txt))
- Use the pybind library [example](./test_compiled_library.py)
- [Optional] Use the python mapper [example](./test_mapped_library.py)
