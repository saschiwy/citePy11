from citePy11 import CitePy11
from citePy11.citepy_config import citepy_config

config = citepy_config()

# Define the header files that should be parsed
config.header_files = ['citePyExample/ExampleLib/AdditionalHeader.h',
                       'citePyExample/ExampleLib/IExample.h']

# [OPTIONAL] Create methods which should be ignored in C++ syntax with full namespace
config.methods_to_ignore = ['CitePyExampleNS::IExample::createLibrary']

# [OPTIONAL] Create methods of classes which should created with custom content
config.custom_methods = {
    'CitePyExampleNS.IExample': ['def __init__(self):\n\tself.__m__ = cpp_m.CitePyExampleNS_IExample.createLibrary()']}

# Create the binding
citepy = CitePy11(config)

## The C++ Binding
cpp = citepy.create_cpp('citePyExample')

with open(f'citePyExample/citePyExample.cpp', 'w') as f:
    f.write(cpp)

## [OPTIONAL] The Python Binding
p = citepy.create_python('citePyExample')

with open(f'citePyExample/citePyExample.py', 'w') as f:
    f.write(p)