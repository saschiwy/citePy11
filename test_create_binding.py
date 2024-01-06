from citePy11 import CitePy11
from citePy11.citepy_config import citepy_config

config = citepy_config()
config.header_files = ['citePyExample/ExampleLib/AdditionalHeader.h',
                       'citePyExample/ExampleLib/IExample.h']

config.custom_python_constructor = {'IExample': 'IExample::createLibrary()'}
config.methods_to_ignore = ['IExample::createLibrary']

header = CitePy11(config)

cpp = header.create_cpp('citePyExample')

with open(f'citePyExample/citePyExample.cpp', 'w') as f:
    f.write(cpp)

p = header.create_python('citePyExample')

with open(f'citePyExample/citePyExample.py', 'w') as f:
    f.write(p)
