#!/usr/bin/python

"""Parse C++ header files and generate a pybind11
binding
"""
import os
import re
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
        self.constant = False
        self.reference = False

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
        self.requireLambda = False

class Property():
    """Represents a property or member variable of a class
    """
    def __init__(self):
        self.name = ""
        self.doxygen = ""

class Typedef():
    def __init__(self):
        self.fullName = ''
        self.name = ''

class Class():
    """Represents a C++ Class
    """
    def __init__(self):
        self.name = ""
        self.methods = []
        self.namespace = ""
        self.doxygen = ""
        self.properties = []
        self.typedefs = []
        self.isAbstract = False

class CitePy11():
    """This class is the main entry Point for the functionality!
    """
    def __init__(self):
        """Initialize the InterfaceHeader class with the path to the desired Header File
        """ 

    def parse(self, headerFile: list):
        """parse the file specifed at Class construction

        Args:
            headerFile (str): Path to the header file which shall be parsed
        """

        self.classes = []
        self.enums = []
        self.filenames = []
        self.typedefs = []

        for header in headerFile:
            self.filenames.append(os.path.basename(header))

            content = ''
            with open(header, 'r') as f:
                content = self.__fixContent__(f.read())

            self.header = cp.CppHeader(content, argType='string')

            for e in self.header.enums:
                self.enums.append(self.__parseEnum__(e))
            for cl in self.header.classes:
                self.classes.append(self.__parseClass__(cl))
            for d in self.header.typedefs:
                self.typedefs.append(self.__parseTypedef__(d))

        for c in self.classes:
            hasConstructor = False
            for m in c.methods:
                for i, arg in enumerate(m.arguments):
                    m.arguments[i].type = self.__fullType__(arg.type)
                
                if m.isConstructor:
                    hasConstructor = True

            if not hasConstructor and not c.isAbstract:
                m = Method()
                m.isConstructor = True
                m.name = c.name
                m.namespace = c.namespace
                m.doxygen = 'Autogenerated constructor'
                c.methods.append(m)

            

    def createBinding(self, targetFile: str, moduleName: str):
        """Creates the binding of the header and writes it to the specified file

        Args:
            targetFile (str): Path to the target cpp file
            moduleName (str): The name the module shall have. Should be the same like the filename
        """
        content = """/* This File is autogenerated with citePy11 (https://github.com/saschiwy/citePy11)
 * author: Sascha Schiwy
 */
        
#include <pybind11/functional.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

"""
        for f in self.filenames:
            content += '#include "' + f + '"\n'

        content += """
namespace py = pybind11;
PYBIND11_MODULE(""" + moduleName + """, m)
{
    /// ---- Declarations ---- ///   
"""
        for enum in self.enums:
            content += '\t' + 'py::enum_<' + enum.namespace + enum.name + '> ' + \
                self.__lowerFirst__(enum.name) + '(m, "' +  enum.name + '"' + self.__addDescription__(enum.doxygen) + ');\n'

        for c in self.classes:
            content += '\tpy::class_<' + c.namespace + '::' + c.name + '> ' + self.__lowerFirst__(c.name) + '(m, "' + c.name + '"' + self.__addDescription__(c.doxygen) + ');\n'

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

                content += '\t\t.def_property_readonly_static("' + m.name + '", []('
                
                for i, arg in enumerate(m.arguments):
                    content += arg.type + ' ' + arg.name
                    if i < len(m.arguments) - 1:
                        content += ', '
                    
                content += '){return ' + c.namespace + '::' + c.name + '::' + m.name + '('
                
                for i, arg in enumerate(m.arguments):
                    content += arg.name
                    if i < len(m.arguments) - 1:
                        content += ', '

                content += ');}'+ self.__addDescription__(m.doxygen) + ')\n'

            content += '\n\t\t/// Member Variables\n'
            for prop in c.properties:
                content += '\t\t.def_readwrite("' + prop.name + '", &' + c.namespace + '::' + c.name + '::' + prop.name + \
                    self.__addDescription__(prop.doxygen) + ')\n'

            content += '\n\t\t/// Constructors\n'
            for m in c.methods:
                if not m.isConstructor:
                    continue

                content += '\t\t.def(py::init<'
                
                for i, arg in enumerate(m.arguments):
                    content += arg.type
                    if i < len(m.arguments) - 1:
                        content += ', '
                
                content += '>()' + self.__addDescription__(m.doxygen) + ')\n'

            content += '\n\t\t/// Member Methods\n'
            for m in c.methods:
                if m.isStatic:
                    continue
                if m.isConstructor:
                    continue
                if m.requireLambda:
                    continue
                content += '\t\t.def("' + m.name + '", py::overload_cast<'
                
                for i, arg in enumerate(m.arguments):
                    content += arg.type
                    if i < len(m.arguments) - 1:
                        content += ', '
                
                content += '>(&' + c.namespace + '::' + c.name + '::' + m.name + ')'
                content += self.__addDescription__(m.doxygen) + ')\n'

            ## Insert those with lambda wrapping
            for m in c.methods:
                if not m.requireLambda or m.isStatic:
                    continue
                
                inOutVals = []

                for arg in m.arguments:
                    if(arg.reference and not arg.constant):
                        inOutVals.append(arg)

                content += '\t\t.def("{0}", []({1}::{2}& self'.format(m.name, c.namespace, c.name)
                for arg in m.arguments:
                    content += ', {} {}'.format(arg.type, arg.name)
                content += ') {'
                for arg in inOutVals:
                    content += '{0} __{1} = {1}; '.format(arg.type.replace('&', '').strip(), arg.name.replace('&', '').strip())
                
                if m.returnType != 'void':
                    content += 'const auto __returnCode = '
                content += 'self.{0}('.format(m.name)
                
                for i, arg in enumerate(m.arguments):
                    if arg in inOutVals:
                        content += '__'
                    content += arg.name
                    if i < len(m.arguments) - 1:
                        content += ', '

                content += '); return std::make_tuple('
                if m.returnType != 'void':
                    content += '__returnCode, '
                
                for i, arg in enumerate(inOutVals):
                    content += '__' + arg.name
                    if i < len(inOutVals) - 1:
                        content += ', '
                content += '); }' + self.__addDescription__(m.doxygen) + ')\n'

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
        result  =  argType.replace('&', '').replace('*', '').replace('const', '').strip()

        try:
            ind = [i for i, c in enumerate(self.classes) if c.name == result]
            result = self.classes[ind[0]].namespace + '::' + self.classes[ind[0]].name
        except : None
        try:
            ind = [i for i, e in enumerate(self.enums) if e.name == result]
            result = self.enums[ind[0]].namespace + self.enums[ind[0]].name
        except : None
        try:
            ind = [i for i, e in enumerate(self.typedefs) if e.name == result]
            result = self.typedefs[ind[0]].fullName
        except : None

        if 'const' in argType:
            result = 'const ' + result

        for i in range(0,argType.count('&')):
            result += '&'

        for i in range(0,argType.count('*')):
            result += '*'

        return result

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

        if 'doxygen' in enumDictionary:
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
        argument.constant = argDictonary['constant']
        argument.reference = argDictonary['reference']
        return argument

    def __parseMethod__(self, methodDictionary):
        """Parse a method struct out of the dictionary Struct of CppHeaderParser

        Args:
            methodDictionary (dict): The Cpp Header Parser Dictonary

        Returns:
            Method: The parsed Method
        """
        method = Method()
        method.name = methodDictionary['name'].strip()
        method.returnType = methodDictionary['returns'].strip()
        method.namespace = methodDictionary['namespace'].strip()
        method.isStatic = methodDictionary['static']

        if 'doxygen' in methodDictionary:
            method.doxygen = methodDictionary['doxygen'].strip()
        
        method.isConstructor = methodDictionary['constructor']

        for arg in methodDictionary['parameters']:
            result = self.__parseArgument__(arg)
            method.arguments.append(result)
            if(result.reference and not result.constant):
                method.requireLambda = True
        
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

        if 'doxygen' in propertyDictionary:
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
        
        if 'doxygen' in self.header.classes[classDictionary]:
            cl.doxygen = self.header.classes[classDictionary]['doxygen']

        for method in self.header.classes[classDictionary]["methods"]["public"]:
            if method['destructor'] or method['template']:
                continue
            cl.methods.append(self.__parseMethod__(method))

        for prop in self.header.classes[classDictionary]["properties"]["public"]:
            cl.properties.append(self.__parseProperty__(prop))
        
        cl.isAbstract = self.header.classes[classDictionary]['abstract']
        return cl

    def __parseTypedef__(self, typedefsDict):
        """Parse a Typedefinition

        Args:
            typedefsDict (dict): The Typedefinitions
        
        Returns:
            Typedef: The parsed Typedefinition
        """

        typedef = Typedef()
        typedef.name = typedefsDict[typedefsDict.rfind('::') +2:]
        typedef.fullName = typedefsDict

        return typedef

    def __fixContent__(self, content):

        # Enum Class is not detected properly by cppHeaderParser
        content = content.replace('enum class', 'enum')

        # Standart Initiatlization is not detected properly by CppHeaderParser
        # https://github.com/robotpy/robotpy-cppheaderparser/issues/63
        #   Always like:  Type Name {maybeSomething};
        lines = content.splitlines()

        content = ''
        for line in lines:
            if '{' in line and '}' in line and ';' in line and '(' not in line and ')' not in line:
                line = line.split('{')[0] + ';'
            content += line + '\n'
        
        return content

    def __addDescription__(self, description):
        if len(description) > 0:
            return ', R"('+ description + ')"'
        else:
            return ''

def parse(headerFile : list):
    """Creates the CitePy11 class and acceses parse method and then returing it.
    Used as a faster access to the implementation

    Args:
        headerFile (str): The file which shall be parsed and created binding for later on

    Returns:
        CitePy11: The binding creator class
    """
    r = CitePy11()
    r.parse(headerFile)

    return r