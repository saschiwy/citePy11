 # This File is autogenerated with citePy11 (Author: Sascha Schiwy)
        
import os
import sys
import enum

script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_path)

import __citePyExample__ as cpp_m

class MyInteger(cpp_m.MyInteger):
    def __init__(self, *args):
        """
        Parameter:
          - Variant 0:
            -- (void)
          - Variant 1:
            -- (int) 
        """

        if len(args) == 0:
            super().__init__()

        elif len(args) == 1:
            super().__init__(args[0])

        else:
            raise Exception("No matching method found for __init__")

    def __add__(self, *args):
        """
        Parameter:
          - Variant 0:
            -- (const MyInteger&) 
          - Variant 1:
            -- (const int&) 
        """

        if len(args) == 1:
            return super().__add__(args[0])

        else:
            raise Exception("No matching method found for __add__")

    def __sub__(self, *args):
        """
        Parameter:
          - Variant 0:
            -- (const MyInteger&) 
          - Variant 1:
            -- (const int&) 
        """

        if len(args) == 1:
            return super().__sub__(args[0])

        else:
            raise Exception("No matching method found for __sub__")

    def __mul__(self, *args):
        """
        Parameter:
          - Variant 0:
            -- (const MyInteger&) 
          - Variant 1:
            -- (const int&) 
        """

        if len(args) == 1:
            return super().__mul__(args[0])

        else:
            raise Exception("No matching method found for __mul__")

    def __truediv__(self, *args):
        """
        Parameter:
          - Variant 0:
            -- (const MyInteger&) 
          - Variant 1:
            -- (const int&) 
        """

        if len(args) == 1:
            return super().__truediv__(args[0])

        else:
            raise Exception("No matching method found for __truediv__")

    def __eq__(self, *args):
        """
        Parameter:
          - Variant 0:
            -- (const MyInteger&) 
          - Variant 1:
            -- (const int&) 
        """

        if len(args) == 1:
            return super().__eq__(args[0])

        else:
            raise Exception("No matching method found for __eq__")

    def __ne__(self, *args):
        """
        Parameter:
          - Variant 0:
            -- (const MyInteger&) 
          - Variant 1:
            -- (const int&) 
        """

        if len(args) == 1:
            return super().__ne__(args[0])

        else:
            raise Exception("No matching method found for __ne__")

    def __lt__(self, *args):
        """
        Parameter:
          - Variant 0:
            -- (const MyInteger&) 
          - Variant 1:
            -- (const int&) 
        """

        if len(args) == 1:
            return super().__lt__(args[0])

        else:
            raise Exception("No matching method found for __lt__")

    def __le__(self, *args):
        """
        Parameter:
          - Variant 0:
            -- (const MyInteger&) 
          - Variant 1:
            -- (const int&) 
        """

        if len(args) == 1:
            return super().__le__(args[0])

        else:
            raise Exception("No matching method found for __le__")

    def __gt__(self, *args):
        """
        Parameter:
          - Variant 0:
            -- (const MyInteger&) 
          - Variant 1:
            -- (const int&) 
        """

        if len(args) == 1:
            return super().__gt__(args[0])

        else:
            raise Exception("No matching method found for __gt__")

    def __ge__(self, *args):
        """
        Parameter:
          - Variant 0:
            -- (const MyInteger&) 
          - Variant 1:
            -- (const int&) 
        """

        if len(args) == 1:
            return super().__ge__(args[0])

        else:
            raise Exception("No matching method found for __ge__")

    def getValue(self, *args):
        """
        Parameter:
          - Variant 0:
            -- (void)
        """

        if len(args) == 0:
            return super().getValue()

        else:
            raise Exception("No matching method found for getValue")

    @staticmethod
    def add(*args):
        """
        Parameter:
          - Variant 0:
            -- (MyInteger) 
            -- (MyInteger) 
        """

        if len(args) == 2:
            return cpp_m.MyInteger.add(args[0], args[1])

        else:
            raise Exception("No matching method found for add")

class SecondNamespace:
    class ExternalStruct(cpp_m.SecondNamespace_ExternalStruct):
        class Test(cpp_m.SecondNamespace_ExternalStruct_Test):
            a = cpp_m.SecondNamespace_ExternalStruct_Test.a
            b = cpp_m.SecondNamespace_ExternalStruct_Test.b

        @property
        def testEnum(self):
            return super(SecondNamespace.ExternalStruct, SecondNamespace.ExternalStruct).testEnum.__get__(self)

        @testEnum.setter
        def testEnum(self, value):
            super(SecondNamespace.ExternalStruct, SecondNamespace.ExternalStruct).testEnum.__set__(self, value)

        @property
        def exampleDouble(self):
            return super(SecondNamespace.ExternalStruct, SecondNamespace.ExternalStruct).exampleDouble.__get__(self)

        @exampleDouble.setter
        def exampleDouble(self, value):
            super(SecondNamespace.ExternalStruct, SecondNamespace.ExternalStruct).exampleDouble.__set__(self, value)

        @property
        def listWithNumbersToAdd(self):
            return super(SecondNamespace.ExternalStruct, SecondNamespace.ExternalStruct).listWithNumbersToAdd.__get__(self)

        @listWithNumbersToAdd.setter
        def listWithNumbersToAdd(self, value):
            super(SecondNamespace.ExternalStruct, SecondNamespace.ExternalStruct).listWithNumbersToAdd.__set__(self, value)

        def __init__(self, *args):
            """
            Parameter:
              - Variant 0:
                -- (void)
            """

            if len(args) == 0:
                super().__init__()

            else:
                raise Exception("No matching method found for __init__")

    class ExternalStruct2(cpp_m.SecondNamespace_ExternalStruct2):
        @property
        def testEnum(self):
            return super(SecondNamespace.ExternalStruct2, SecondNamespace.ExternalStruct2).testEnum.__get__(self)

        @testEnum.setter
        def testEnum(self, value):
            super(SecondNamespace.ExternalStruct2, SecondNamespace.ExternalStruct2).testEnum.__set__(self, value)

        def __init__(self, *args):
            """
            Parameter:
              - Variant 0:
                -- (void)
            """

            if len(args) == 0:
                super().__init__()

            else:
                raise Exception("No matching method found for __init__")

class four:
    class namespaces:
        class at:
            class once:
                class ExternalStruct3(cpp_m.four_namespaces_at_once_ExternalStruct3):
                    @property
                    def testInt(self):
                        return super(four.namespaces.at.once.ExternalStruct3, four.namespaces.at.once.ExternalStruct3).testInt.__get__(self)

                    @testInt.setter
                    def testInt(self, value):
                        super(four.namespaces.at.once.ExternalStruct3, four.namespaces.at.once.ExternalStruct3).testInt.__set__(self, value)

                    def setTestInt(self, *args):
                        """
                          - Set the testInt value
                        Parameter:
                          - Variant 0:
                            -- (int)  value
                        Returns:
                          - int
                        """

                        if len(args) == 1:
                            return super().setTestInt(args[0])

                        else:
                            raise Exception("No matching method found for setTestInt")

                    def __init__(self, *args):
                        """
                        Parameter:
                          - Variant 0:
                            -- (void)
                        """

                        if len(args) == 0:
                            super().__init__()

                        else:
                            raise Exception("No matching method found for __init__")

class CitePyExampleNS:
    class ExampleEnum(cpp_m.CitePyExampleNS_ExampleEnum):
        """
          - Values that represent example enums
        """

        add = cpp_m.CitePyExampleNS_ExampleEnum.add
        subtract = cpp_m.CitePyExampleNS_ExampleEnum.subtract

    class ExampleStruct(cpp_m.CitePyExampleNS_ExampleStruct):
        """
          - An example structure.
        """

        @property
        def left(self):
            """The left"""
            return super(CitePyExampleNS.ExampleStruct, CitePyExampleNS.ExampleStruct).left.__get__(self)

        @left.setter
        def left(self, value):
            super(CitePyExampleNS.ExampleStruct, CitePyExampleNS.ExampleStruct).left.__set__(self, value)

        @property
        def right(self):
            """The right"""
            return super(CitePyExampleNS.ExampleStruct, CitePyExampleNS.ExampleStruct).right.__get__(self)

        @right.setter
        def right(self, value):
            super(CitePyExampleNS.ExampleStruct, CitePyExampleNS.ExampleStruct).right.__set__(self, value)

        def __init__(self, *args):
            """
              - Default constructor
              - Constructor
            Parameter:
              - Variant 0:
                -- (void)
              - Variant 1:
                -- (double)  left    The left.
                -- (double)  right   The right.
            Function:
              - ExampleStruct();
              - ExampleStruct(double left, double right);
            """

            if len(args) == 0:
                super().__init__()

            elif len(args) == 2:
                super().__init__(args[0], args[1])

            else:
                raise Exception("No matching method found for __init__")

        def set(self, *args):
            """
            Parameter:
              - Variant 0:
                -- (T) 
                -- (T) 
              - Variant 1:
                -- (double) 
            """

            if len(args) == 2:
                return super().set(args[0], args[1])

            elif len(args) == 1:
                return super().set(args[0])

            else:
                raise Exception("No matching method found for set")

        def getLeft(self, *args):
            """
            Parameter:
              - Variant 0:
                -- (void)
            """

            if len(args) == 0:
                return super().getLeft()

            else:
                raise Exception("No matching method found for getLeft")

    class IExample:
        """
          - An example class to show the usage ot citePy
        """

        def add(self, *args):
            """
              - Adds two doubles
            Parameter:
              - Variant 0:
                -- (double)  left    The left.
                -- (double)  right   The right.
            Returns:
              - the result.
            Function:
              - virtual double IExample::add(double left, double right) = 0;
            """

            if len(args) == 2:
                return self.__m__.add(args[0], args[1])

            else:
                raise Exception("No matching method found for add")

        def subtract(self, *args):
            """
              - Subtracts two doubles
            Parameter:
              - Variant 0:
                -- (double)  left    The left.
                -- (double)  right   The right.
            Returns:
              - the result.
            Function:
              - virtual double IExample::subtract(double left, double right) = 0;
            """

            if len(args) == 2:
                return self.__m__.subtract(args[0], args[1])

            else:
                raise Exception("No matching method found for subtract")

        def compute(self, *args):
            """
              - Computes with an enum operator and the values inside the example structure
              - Adds all the given values, inside the vector
              - Computes the given values
            Parameter:
              - Variant 0:
                -- (ExampleEnum)  option  The option.
                -- (ExampleStruct)  values  The values.
              - Variant 1:
                -- (const std::vector<double>&)  values  The values.
              - Variant 2:
                -- (SecondNamespace::ExternalStruct)  values  The values.
            Returns:
              - the result.
              - A double.
              - A double.
            Function:
              - virtual double IExample::compute(ExampleEnum option, ExampleStruct values) = 0;
              - virtual double IExample::compute(SecondNamespace::ExternalStruct values) = 0;
              - virtual double IExample::compute(SecondNamespace::ExternalStruct values) = 0;
            """

            if len(args) == 2:
                return self.__m__.compute(args[0], args[1])

            elif len(args) == 1:
                return self.__m__.compute(args[0])

            else:
                raise Exception("No matching method found for compute")

        def registerCallback(self, *args):
            """
              - Registers the callback described by cb
            Parameter:
              - Variant 0:
                -- (ExampleCallbackDefinition)  cb  The cb.
            Function:
              - virtual void IExample::registerCallback(ExampleCallbackDefinition cb) = 0;
            """

            if len(args) == 1:
                return self.__m__.registerCallback(args[0])

            else:
                raise Exception("No matching method found for registerCallback")

        def addReferenced(self, *args):
            """
              - Adds a referenced
            Parameter:
              - Variant 0:
                -- (double&)  [in,out]  result  The result.
                -- (double)  left    The left.
                -- (double)  right   The right.
            Function:
              - virtual void IExample::addReferenced(double& result, double left, double right) = 0;
            """

            if len(args) == 3:
                return self.__m__.addReferenced(args[0], args[1], args[2])

            else:
                raise Exception("No matching method found for addReferenced")

        def __init__(self):
            self.__m__ = cpp_m.CitePyExampleNS_IExample.createLibrary()

