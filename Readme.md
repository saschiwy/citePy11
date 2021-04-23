# CPP Interface Translation Engine for Pybind11 (CitePy11)

## Introduction
The engine intends to create pybind11 bindings out of a CPP Interface Header.

## Required Software
- CMake >= 3.14
- A CMake compatible compiler
- python >= 3.7
- [robotpy CppHeaderParser](https://github.com/robotpy/robotpy-cppheaderparser)
~~~~
pip install robotpy-cppheaderparser
~~~~ 
- [pybind11](https://github.com/pybind/pybind11) With CMake Support (either via conda install or clone and build yourself)

## Install:
- Fullfil the requirements
- Clone this repo
- Install the software
~~~~
pip install ./citePy11
~~~~

## Example Usage:
### Create the binding

You find the example in the subfolder citePyExample. To create the binding use:

~~~~{.py}
from citePy11 import CitePy11 as CitePy
header = CitePy()
header.parse('citePyExample/ExampleLib/IExample.h')
header.createBinding('citePyExample/citePyExample.cpp', 'citePyExample')
~~~~

### Install the library
~~~~
pip install ./citePyExample
~~~~

### Use it:
~~~~{.py}
import citePyExample
lib = citePyExample.IExample.createLibrary

exampleStruct = citePyExample.ExampleStruct(5.0,3.0)

print(lib.compute(citePyExample.ExampleEnum.subtract, exampleStruct))
print(lib.add(1.1, 1.2))

>>> 2.0
>>> 2.3
~~~~