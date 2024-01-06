#!/usr/bin/python

"""
Parse C++ header files and generate a pybind11
binding
"""
import os
import re
from cxxheaderparser.simple import parse_string
from citePy11.code_dump import CodeDump
from citePy11.citepy_config import citepy_config

version = __version__ = "0.1.0"


class CitePy11:
    """
    This class is the main entry Point for the functionality!
    """

    def __init__(self, config: citepy_config):
        """
        Initialize the InterfaceHeader class with the path to the desired Header File
        """
        self.config = config
        self.header_files = config.header_files
        self.filenames = []
        self.contents = []

        self.dump = CodeDump(self.config)
        self.dump.no_doc = True

        self.__parse__()

    def __parse__(self):
        """
        parse the file specified at Class construction

        Args:
            header_file (str): Path to the header file which shall be parsed
        """

        for header in self.header_files:
            filename = os.path.basename(header)
            self.filenames.append(filename)

            with open(header, 'r') as f:
                #     content = self.__fix_content__(f.read())
                self.contents.append(parse_string(f.read(), filename=filename))

    def create_cpp(self, module_name):
        """
        Create the cpp content, of all files
        """

        result = self.dump.get_cpp_head(self.filenames)
        result = self.dump.add_module(result, module_name)

        for i in range(len(self.filenames)):
            result += self.__create_cpp__(self.contents[i], self.filenames[i])
        result = self.dump.close_module(result)
        return result

    def __create_cpp__(self, content, header_file):
        """
        Create the cpp content, of one file
        """

        result = ''
        content = content.namespace
        namespace_prefix = ''

        result = self.__add_namespace__(result, content, namespace_prefix)

        for namespace in content.namespaces:
            t = content.namespaces[namespace]
            result = self.__add_namespace__(result, t, namespace_prefix + namespace + '::')

        return result

    def __add_namespace__(self, result, content, namespace_prefix):
        self.dump.find_typedefs(content, namespace_prefix)
        result = self.dump.add_enums(result, content.enums, namespace_prefix)
        result = self.dump.add_functions(result, content.functions, namespace_prefix)
        result = self.dump.add_classes(result, content.classes, namespace_prefix)
        return result

    def create_python(self, module_name):
        """
        Create the python content, of all files
        """

        result = self.dump.get_python_head(module_name)
        result = self.dump.get_python_content(result, self.contents)

        return result
