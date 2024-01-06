/* This File is autogenerated with citePy11 (https://github.com/saschiwy/citePy11)
 * author: Sascha Schiwy
 */

// Solve VS2022 Bug https://www.reddit.com/r/cpp_questions/comments/qpo93t/error_c2039_invalid_parameter_is_not_a_member_of/
#ifdef _WIN32
#include <corecrt.h>
#endif
        
#include <pybind11/functional.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "AdditionalHeader.h"
#include "IExample.h"
    

namespace py = pybind11;

PYBIND11_MODULE(__citePyExample__, m) {
py::enum_<SecondNamespace::ExternalStruct::Test> (m, "SecondNamespace_ExternalStruct_Test")
	.value("a", SecondNamespace::ExternalStruct::Test::a)
	.value("b", SecondNamespace::ExternalStruct::Test::b)
	.export_values();

py::class_<SecondNamespace::ExternalStruct> (m, "SecondNamespace_ExternalStruct")
.def_readwrite("testEnum", &SecondNamespace::ExternalStruct::testEnum)
.def_readwrite("exampleDouble", &SecondNamespace::ExternalStruct::exampleDouble)
.def_readwrite("listWithNumbersToAdd", &SecondNamespace::ExternalStruct::listWithNumbersToAdd)
.def(py::init<>());

py::enum_<CitePyExampleNS::ExampleEnum> (m, "CitePyExampleNS_ExampleEnum")
	.value("add", CitePyExampleNS::ExampleEnum::add)
	.value("subtract", CitePyExampleNS::ExampleEnum::subtract)
	.export_values();

py::class_<CitePyExampleNS::ExampleStruct> (m, "CitePyExampleNS_ExampleStruct")
.def_readwrite("left", &CitePyExampleNS::ExampleStruct::left)
.def_readwrite("right", &CitePyExampleNS::ExampleStruct::right)
.def(py::init<>())
.def(py::init<double, double>())
.def("getLeft", py::overload_cast<>(&CitePyExampleNS::ExampleStruct::getLeft, py::const_))
;

py::class_<CitePyExampleNS::IExample> (m, "CitePyExampleNS_IExample")
.def_static("createLibrary", py::overload_cast<>(&CitePyExampleNS::IExample::createLibrary))
.def("add", py::overload_cast<double, double>(&CitePyExampleNS::IExample::add, py::const_))
.def("subtract", py::overload_cast<double, double>(&CitePyExampleNS::IExample::subtract))
.def("compute", py::overload_cast<CitePyExampleNS::ExampleEnum, CitePyExampleNS::ExampleStruct>(&CitePyExampleNS::IExample::compute))
.def("compute", py::overload_cast<const std::vector<double>&>(&CitePyExampleNS::IExample::compute))
.def("compute", py::overload_cast<SecondNamespace::ExternalStruct>(&CitePyExampleNS::IExample::compute))
.def("registerCallback", py::overload_cast<CitePyExampleNS::ExampleCallbackDefinition>(&CitePyExampleNS::IExample::registerCallback))
.def("addReferenced", [](CitePyExampleNS::IExample& self, double& result, double left, double right) {auto __result = result; self.addReferenced(result, left, right); return std::make_tuple(__result); })
;

}
