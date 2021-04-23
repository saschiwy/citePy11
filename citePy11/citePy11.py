#!/usr/bin/python

"""Parse C++ header files and generate a pybind11
binding
"""
import os
import CppHeaderParser as cp
version = __version__ = "0.0.1"


class Enum():
    """Represents an CPP Enum and it's values
    """
    def __init__(self):
        self.name = ""
        self.namespace = ""
        self.options = []
        self.optDesc = []
        self.doxygen = ""

class Argument():
    """Represents a argument or parameter which is given to a method
    """
    def __init__(self):
        self.name = ""
        self.type = ""

class Method():
    """Represents a member method of a class
    """
    def __init__(self):
        self.name = ""
        self.returnType = ""
        self.namespace = ""
        self.isStatic = False
        self.isConstructor = False
        self.arguments = []
        self.doxygen = ""

class Property():
    """Represents a property or member variable of a class
    """
    def __init__(self):
        self.name = ""
        self.doxygen = ""

class Class():
    """Represents a C++ Class
    """
    def __init__(self):
        self.name = ""
        self.methods = []
        self.namespace = ""
        self.doxygen = ""
        self.properties = []

class CitePy11():
    """This class is the main entry Point for the functionality!
    """
    def __init__(self):
        """Initialize the InterfaceHeader class with the path to the desired Header File
        """ 

    def parse(self, headerFile):
        """parse the file specifed at Class construction

        Args:
            headerFile (str): Path to the header file which shall be parsed
        """

        self.classes = []
        self.enums = []
        with open(headerFile, 'r') as f:
            self.content = f.read()
        self.filename = os.path.basename(headerFile)

        self.content = self.content.replace('enum class', 'enum')
        self.header = cp.CppHeader(self.content, argType='string')

        for e in self.header.enums:
            self.enums.append(self.__parseEnum__(e))
        for cl in self.header.classes:
            self.classes.append(self.__parseClass__(cl))
        for c in self.classes:
            for m in c.methods:
                for i, arg in enumerate(m.arguments):
                    m.arguments[i].type = self.__fullType__(arg.type)

    def createBinding(self, targetFile: str, moduleName: str):
        """Creates the binding of the header and writes it to the specified file

        Args:
            targetFile (str): Path to the target cpp file
            moduleName (str): The name the module shall have. Should be the same like the filename
        """
        content = """#include <pybind11/functional.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include \"""" + self.filename + """\"

namespace py = pybind11;
PYBIND11_MODULE(""" + moduleName + """, m)
{
    /// ---- Declarations ---- ///   
"""
        for enum in self.enums:
            content += '\t' + 'py::enum_<' + enum.namespace + enum.name + '> ' + \
                self.__lowerFirst__(enum.name) + '(m, "' +  enum.name + '", R"('+ enum.doxygen+ ')");\n'

        for c in self.classes:
            content += '\tpy::class_<' + c.namespace + '::' + c.name + '> ' + self.__lowerFirst__(c.name) + '(m, "' + c.name + '", R"(' + c.doxygen + ')");' + '\n'

        content += '\n\t/// ---- Enum definitions ---- ///\n'
        for enum in self.enums:
            content += '\t' + self.__lowerFirst__(enum.name) + '\n'
            for opt in enum.options:
                content += '\t\t.value("' + opt + \
                '", ' + enum.namespace + enum.name + '::' + opt + ')\n'
            content += '\t\t.export_values();\n'

        ## Class Definitions
        content += '\n\t/// ---- Class definitions ---- ///\n'
        for c in self.classes:
            content += '\t' + self.__lowerFirst__(c.name) + '\n' \
                    + '\t\t/// Static Methods\n'
            for m in c.methods:
                if not m.isStatic:
                    continue
                content += '\t\t.def_property_readonly_static("' + m.name + '", [](py::object){return ' \
                    + c.namespace + '::' + c.name + '::' + m.name + '('
                
                for i, arg in enumerate(m.arguments):
                    content += arg.type + ' ' + arg.name
                    if i < len(m.arguments) - 1:
                        content += ', '

                content += ');}, R"(' + m.doxygen + ')")\n'

            content += '\n\t\t/// Member Variables\n'
            for prop in c.properties:
                content += '\t\t.def_readwrite("' + prop.name + '", &' + c.namespace + '::' + c.name + '::' + prop.name + \
                    ', R"(' + prop.doxygen + ')")\n'

            content += '\n\t\t/// Constructors\n'
            for m in c.methods:
                if not m.isConstructor:
                    continue

                content += '\t\t.def(py::init<'
                
                for i, arg in enumerate(m.arguments):
                    content += arg.type
                    if i < len(m.arguments) - 1:
                        content += ', '
                
                content += '>(),'
                content += ' R"(' + m.doxygen + ')")\n'

            content += '\n\t\t/// Member Methods\n'
            for m in c.methods:
                if m.isStatic:
                    continue
                if m.isConstructor:
                    continue
                content += '\t\t.def("' + m.name + '", py::overload_cast<'
                
                for i, arg in enumerate(m.arguments):
                    content += arg.type
                    if i < len(m.arguments) - 1:
                        content += ', '
                
                content += '>(&' + c.namespace + '::' + c.name + '::' + m.name + '),'
                content += ' R"(' + m.doxygen + ')")\n'

            content += '\t;\n\n'
        # End
        content += "}"

        with open(targetFile, 'w') as f:
            f.write(content)

    def __lowerFirst__(self, string : str):
        """Lower the first letter of a string

        Args:
            string (str): The string which shall be manipulated

        Returns:
            str: The resulting string
        """
        if len(string) == 0:
            return string
        else:
            return string[0].lower() + string[1:]

    def __fullType__(self, argType: str):
        """Determines the full cpp type with Namespace and Class prefixes

        Args:
            argType (str): The type without prefixed

        Returns:
            str: The full type with prefixes
        """
        try:
            ind = [i for i, c in enumerate(self.classes) if c.name == argType]
            return self.classes[ind[0]].namespace + '::' + self.classes[ind[0]].name
        except:
            try:
                ind = [i for i, e in enumerate(self.enums) if e.name == argType]
                return self.enums[ind[0]].namespace + self.enums[ind[0]].name
            except:
                return argType

    def __parseEnum__(self, enumDictionary):
        """Parse an enum struct out of the dictionary Struct of CppHeaderParser

        Args:
            enumDictionary (dict): The Cpp Header Parser Dictonary

        Returns:
            Enum: The parsed Enum
        """
        enum = Enum()
        enum.name = enumDictionary['name']
        enum.namespace = enumDictionary['namespace']
        for opt in enumDictionary['values']:
            enum.options.append(opt['name'])
        enum.doxygen = enumDictionary["doxygen"]
        return enum

    def __parseArgument__(self, argDictonary):
        """Parse an argument struct out of the dictionary Struct of CppHeaderParser

        Args:
            argDictionary (dict): The Cpp Header Parser Dictonary

        Returns:
            Argument: The parsed Argument
        """
        argument = Argument()
        argument.name = argDictonary['name']
        argument.type = argDictonary['type']
        return argument

    def __parseMethod__(self, methodDictionary):
        """Parse a method struct out of the dictionary Struct of CppHeaderParser

        Args:
            methodDictionary (dict): The Cpp Header Parser Dictonary

        Returns:
            Method: The parsed Method
        """
        method = Method()
        method.name = methodDictionary['name']
        method.returnType = methodDictionary['returns']
        method.namespace = methodDictionary['namespace']
        method.isStatic = methodDictionary['static']
        method.doxygen = methodDictionary['doxygen']
        method.isConstructor = methodDictionary['constructor']

        for arg in methodDictionary['parameters']:
            method.arguments.append(self.__parseArgument__(arg))
        
        return method

    def __parseProperty__(self, propertyDictionary):
        """Parse a property struct out of the dictionary Struct of CppHeaderParser

        Args:
            propertyDictionary (dict): The Cpp Header Parser Dictonary

        Returns:
            Property: The parsed Property
        """
        prop = Property()
        prop.name = propertyDictionary['name']
        prop.doxygen = propertyDictionary['doxygen']
        return prop

    def __parseClass__(self, classDictionary):
        """Parse a class struct out of the dictionary Struct of CppHeaderParser

        Args:
            classDictionary (dict): The Cpp Header Parser Dictonary

        Returns:
            Class: The parsed Class
        """
        cl = Class()
        cl.name = self.header.classes[classDictionary]['name']
        cl.namespace = self.header.classes[classDictionary]['namespace']
        cl.doxygen = self.header.classes[classDictionary]['doxygen']

        for method in self.header.classes[classDictionary]["methods"]["public"]:
            cl.methods.append(self.__parseMethod__(method))

        for prop in self.header.classes[classDictionary]["properties"]["public"]:
            cl.properties.append(self.__parseProperty__(prop))
        
        return cl