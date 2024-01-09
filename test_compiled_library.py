# import citePyExample.citePyExample as m
import citePyExample.__citePyExample__ as cpp_m


# external_struct = m.SecondNamespace.ExternalStruct()
# external_struct.exampleDouble = 5.0
# print(external_struct.exampleDouble)
#
# example_struct = m.CitePyExampleNS.ExampleStruct(5, 3)
# example_lib = m.CitePyExampleNS.IExample()
#
# example_struct.left = 6
# example_struct.right = 10
#
#
# def cb(value):
#     print(f'Callback: {value}')
#
#
# example_lib.registerCallback(cb)
#
# print(f'ExampleLib.add: {5} + {10} = {example_lib.add(5, 10)}')
# print(f'ExampleLib.compute: {6} + {10} = {example_lib.compute(m.CitePyExampleNS.ExampleEnum.add ,example_struct)}')
# print(f'ExampleLib.addReferenced: {6} + {10} = {example_lib.addReferenced(1, 5, 10)}')

cpp_lib = cpp_m.CitePyExampleNS_IExample.createLibrary()
cpp_lib.registerCallback(lambda x: print(f'Callback: {x}'))

external_struct = cpp_m.SecondNamespace_ExternalStruct()
external_struct.exampleDouble = 5.0
external_struct.listWithNumbersToAdd = [1, 2]

print(f'ExampleLib.compute(Enum, Example Struct: {5} + {10} = {cpp_lib.compute(cpp_m.CitePyExampleNS_ExampleEnum.add, cpp_m.CitePyExampleNS_ExampleStruct(5, 10))}')
print(f'ExampleLib.compute(External Struct: {1} + {2} = {cpp_lib.compute(external_struct)}')
print(f'ExampleLib.compute(List: {1} + {5} = {cpp_lib.compute([1, 5])}')
