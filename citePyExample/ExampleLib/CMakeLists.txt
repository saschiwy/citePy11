cmake_minimum_required (VERSION 3.14)
file(GLOB_RECURSE SOURCES LIST_DIRECTORIES true *.h *.cpp)
add_library(ExampleLib ${SOURCES})