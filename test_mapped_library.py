import pytest
import citePyExample.citePyExample as m

received_callback_values = []
expected_values = []


def callback(value):
    global received_callback_values
    received_callback_values.append(value)


example_lib = m.CitePyExampleNS.IExample()
example_lib.registerCallback(callback)


def external_struct_setter_getter():
    external_struct = m.SecondNamespace.ExternalStruct()
    external_struct.listWithNumbersToAdd = [1, 2]
    external_struct.exampleDouble = 5.0
    external_struct.testEnum = m.SecondNamespace.ExternalStruct.Test.b
    assert len(external_struct.listWithNumbersToAdd) == 2
    assert external_struct.listWithNumbersToAdd[0] == 1
    assert external_struct.listWithNumbersToAdd[1] == 2
    assert external_struct.exampleDouble == 5.0
    assert external_struct.testEnum == m.SecondNamespace.ExternalStruct.Test.b


def test_example_struct_setter_getter():
    example_struct = m.CitePyExampleNS.ExampleStruct()
    example_struct.left = 5
    example_struct.right = 10
    assert example_struct.left == 5
    assert example_struct.right == 10


def test_example_lib_compute_example_struct():
    example_struct = m.CitePyExampleNS.ExampleStruct()
    example_struct.left = 5
    example_struct.right = 10
    assert example_lib.compute(m.CitePyExampleNS.ExampleEnum.add, example_struct) == 15
    assert example_lib.compute(m.CitePyExampleNS.ExampleEnum.subtract, example_struct) == -5

    global expected_values
    expected_values = [15, -5]


def test_example_lib_compute_external_struct():
    external_struct = m.SecondNamespace.ExternalStruct()
    external_struct.listWithNumbersToAdd = [1, 2]
    assert example_lib.compute(external_struct) == 3

    global expected_values
    expected_values.append(3)


def test_example_lib_compute_list():
    expected_result = 6.2
    tolerance = 0.0001

    result = example_lib.compute([1.1, 5.1])

    assert abs(result - expected_result) <= tolerance

    global expected_values
    expected_values.append(expected_result)


def test_example_lib_add():
    assert example_lib.add(10, 2) == 12

    global expected_values
    expected_values.append(12)


def test_example_lib_subtract():
    assert example_lib.subtract(10, 2) == 8

    global expected_values
    expected_values.append(8)


def test_example_lib_add_referenced():
    assert example_lib.addReferenced(22, 10, 2) == 12

    global expected_values
    expected_values.append(12)


def test_callback():
    global received_callback_values
    global expected_values
    tolerance = 0.0001

    assert len(received_callback_values) == len(expected_values)

    for received, expected in zip(received_callback_values, expected_values):
        assert abs(received - expected) <= tolerance


def test_addition():
    my_integer = m.MyInteger(5)
    result = my_integer + 3 == 8

    assert result


def test_subtraction():
    my_integer = m.MyInteger(5)

    result = my_integer - 2
    assert result == 3


def test_multiplication():
    my_integer = m.MyInteger()
    my_integer += 5

    result = my_integer * 2
    assert result == 10


def test_division():
    my_integer = m.MyInteger(5)

    result = my_integer / m.MyInteger(2)
    assert result == 2


def test_equality():
    my_integer = m.MyInteger(5)

    assert my_integer == 5


def test_inequality():
    my_integer = m.MyInteger(5)

    assert my_integer != 4


def test_less_than():
    my_integer = m.MyInteger(5)

    assert my_integer < 10


def test_less_than_or_equal():
    my_integer = m.MyInteger(5)

    assert my_integer <= 5


def test_greater_than():
    my_integer = m.MyInteger(5)

    assert my_integer > 2


def test_greater_than_or_equal():
    my_integer = m.MyInteger(5)

    assert my_integer >= 5


def test_static_add():
    assert m.MyInteger.add(m.MyInteger(5), m.MyInteger(2)) == 7


def test_second_external_struct():
    second_struct = m.SecondNamespace.ExternalStruct2()
    second_struct.testEnum = m.SecondNamespace.ExternalStruct.Test.b

    assert second_struct.testEnum == m.SecondNamespace.ExternalStruct.Test.b
