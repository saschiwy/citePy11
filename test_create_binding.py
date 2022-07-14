import citePy11


header = citePy11.parse(['citePyExample/ExampleLib/AdditionalHeader.h', 'citePyExample/ExampleLib/IExample.h'])
header.create_binding('citePyExample/citePyExample.cpp', 'citePyExample')
