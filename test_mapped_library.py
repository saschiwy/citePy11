import citePyExample.citePyExample as m

example_struct = m.CitePyExampleNS.ExampleStruct(5, 3)
example_lib = m.CitePyExampleNS.IExample.createLibrary()

example_struct.left = 6
example_struct.right = 10


def cb(value):
    print(f'Callback: {value}')


# example_lib.registerCallback(cb)
external_struct = m.SecondNamespace.ExternalStruct()
external_struct.listWithNumbersToAdd = [1, 2]
print('External Struct, listWithNumbersToAdd: ' + str(external_struct.listWithNumbersToAdd))

operation = m.CitePyExampleNS.ExampleEnum.subtract
example_struct = m.CitePyExampleNS.ExampleStruct(5, 10)
res = example_lib.compute(operation, example_struct)
print(f'ExampleLib.compute(Enum, Example Struct: {5} + {10} = {res}')
print(f'ExampleLib.compute(External Struct: {1} + {2} = {example_lib.compute(external_struct)}')
# print(f'ExampleLib.compute(List: {1.1} + {5.1} = {example_lib.compute([1.1, 5.1])}')
