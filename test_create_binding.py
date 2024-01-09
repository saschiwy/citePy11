from citePy11 import CitePy11
from citePy11.citepy_config import citepy_config

config = citepy_config()
config.header_files = ['citePyExample/ExampleLib/AdditionalHeader.h',
                       'citePyExample/ExampleLib/IExample.h']

# config.custom_python_constructor = {
#     'CitePyExampleNS::IExample': 'def __init__()\n'    'self.__m__ = cpp_m.CitePyExampleNS_IExample.createLibrary()'}
# config.methods_to_ignore = ['CitePyExampleNS::IExample::createLibrary']

header = CitePy11(config)

cpp = header.create_cpp('citePyExample')

with open(f'citePyExample/citePyExample.cpp', 'w') as f:
    f.write(cpp)

p = header.create_python('citePyExample')

with open(f'citePyExample/citePyExample.py', 'w') as f:
    f.write(p)
