 # This File is autogenerated with citePy11 (Author: Sascha Schiwy)
        
import os
import sys
import enum

script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_path)

import __citePyExample__ as cpp_m

class SecondNamespace:
    class ExternalStruct(cpp_m.SecondNamespace_ExternalStruct):
        class Test(enum.Enum):
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
            if len(args) == 0:
                super().__init__()
        
            else:
                raise Exception("No matching method found for __init__")
        
        
        
    

class CitePyExampleNS:
    class ExampleEnum(enum.Enum):
        """
        Values that represent example enums
        """
        
        add = cpp_m.CitePyExampleNS_ExampleEnum.add
        subtract = cpp_m.CitePyExampleNS_ExampleEnum.subtract
    
    class ExampleStruct(cpp_m.CitePyExampleNS_ExampleStruct):
        """
        An example structure.
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
            if len(args) == 0:
                super().__init__()
        
            elif len(args) == 2:
                super().__init__(args[0], args[1])
        
            else:
                raise Exception("No matching method found for __init__")
        
        def set(self, *args):
            if len(args) == 2:
                return super().set(args[0], args[1])
        
            else:
                raise Exception("No matching method found for set")
        
        def getLeft(self, *args):
            if len(args) == 0:
                return super().getLeft()
        
            else:
                raise Exception("No matching method found for getLeft")
        
        
        
    
    class IExample(cpp_m.CitePyExampleNS_IExample):
        """
        An example class to show the usage ot citePy
        """
        
        def add(self, *args):
            if len(args) == 2:
                return super().add(args[0], args[1])
        
            else:
                raise Exception("No matching method found for add")
        
        def subtract(self, *args):
            if len(args) == 2:
                return super().subtract(args[0], args[1])
        
            else:
                raise Exception("No matching method found for subtract")
        
        def compute(self, *args):
            if len(args) == 2:
                return super().compute(args[0], args[1])
        
            elif len(args) == 1:
                return super().compute(args[0])
        
            else:
                raise Exception("No matching method found for compute")
        
        def registerCallback(self, *args):
            if len(args) == 1:
                return super().registerCallback(args[0])
        
            else:
                raise Exception("No matching method found for registerCallback")
        
        def addReferenced(self, *args):
            if len(args) == 3:
                return super().addReferenced(args[0], args[1], args[2])
        
            else:
                raise Exception("No matching method found for addReferenced")
        
        def __init__(self, *args):
            if len(args) == 0:
                super().__init__()
        
            else:
                raise Exception("No matching method found for __init__")
        
        
        @staticmethod
        def createLibrary(*args):
            if len(args) == 0:
                return cpp_m.CitePyExampleNS_IExample.createLibrary()
        
            else:
                raise Exception("No matching method found for createLibrary")
        
        
    

