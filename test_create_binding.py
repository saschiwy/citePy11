from citePy11 import CitePy11

header = CitePy11(header_files=['citePyExample/ExampleLib/AdditionalHeader.h',
                                'citePyExample/ExampleLib/IExample.h'])

cpp = header.create_cpp('citePyExample')

with open(f'citePyExample/citePyExample.cpp', 'w') as f:
    f.write(cpp)

p = header.create_python('citePyExample')

with open(f'citePyExample/citePyExample.py', 'w') as f:
    f.write(p)
