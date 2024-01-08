import citePyExample.citePyExample as m

external_struct = m.SecondNamespace.ExternalStruct()
external_struct.exampleDouble = 5.0
print(external_struct.exampleDouble)

example_struct = m.CitePyExampleNS.ExampleStruct(5, 3)
example_lib = m.CitePyExampleNS.IExample()

example_struct.left = 6
example_struct.right = 10


def cb(value):
    print(f'Callback: {value}')


example_lib.registerCallback(cb)

print(f'ExampleLib.add: {5} + {10} = {example_lib.add(5, 10)}')
print(f'ExampleLib.compute: {6} + {10} = {example_lib.compute(m.CitePyExampleNS.ExampleEnum.add ,example_struct)}')
print(f'ExampleLib.addReferenced: {6} + {10} = {example_lib.addReferenced(1, 5, 10)}')
