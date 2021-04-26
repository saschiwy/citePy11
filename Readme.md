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
import citePy11
header  = citePy11.parse(['citePyExample/ExampleLib/AdditionalHeader.h', 'citePyExample/ExampleLib/IExample.h'])
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

## Known Issues:
- [Struct members with default initialiser lists are unparsed](https://github.com/robotpy/robotpy-cppheaderparser/issues/63)
  - CitePy tries to workaround this issue by some specific line attriubte replacements, like it's done in Additional Header example
- enum class is not detected as enum. CitePy11 resolves this by replacing 'enum class' with 'enum' only during parsing
- [Class Internal Typedefs are not parsed](https://github.com/robotpy/robotpy-cppheaderparser/issues/68)