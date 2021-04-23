#include <pybind11/functional.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "IExample.h"

namespace py = pybind11;
PYBIND11_MODULE(citePyExample, m)
{
    /// ---- Declarations ---- ///   
	py::enum_<CitePyExampleNS::ExampleEnum> exampleEnum(m, "ExampleEnum", R"(/*!
* \enum    ExampleEnum
*
* \brief   Values that represent example enums
*/)");
	py::class_<CitePyExampleNS::ExampleStruct> exampleStruct(m, "ExampleStruct", R"(/*!
* \struct  ExampleStruct
*
* \brief   An example structure.
*/)");
	py::class_<CitePyExampleNS::IExample> iExample(m, "IExample", R"(/*!
* \class   IExample
*
* \brief   An example class to show the usage ot citePy
*/)");

	/// ---- Enum definitions ---- ///
	exampleEnum
		.value("add", CitePyExampleNS::ExampleEnum::add)
		.value("subtract", CitePyExampleNS::ExampleEnum::subtract)
		.export_values();

	/// ---- Class definitions ---- ///
	exampleStruct
		/// Static Methods

		/// Member Variables
		.def_readwrite("left", &CitePyExampleNS::ExampleStruct::left, R"(///< The left)")
		.def_readwrite("right", &CitePyExampleNS::ExampleStruct::right, R"(///< The right)")

		/// Constructors
		.def(py::init<>(), R"(/*!
* \fn  ExampleStruct();
*
* \brief   Default constructor
*/)")
		.def(py::init<double, double>(), R"(/*!
* \fn  ExampleStruct(double left, double right);
*
* \brief   Constructor
*
* \param   left    The left.
* \param   right   The right.
*/)")

		/// Member Methods
	;

	iExample
		/// Static Methods
		.def_property_readonly_static("createLibrary", [](py::object){return CitePyExampleNS::IExample::createLibrary();}, R"(/*!
* \fn  static std::unique_ptr<IExample> IExample::createLibrary();
*
* \brief   Instantiates a library object without knowledge about the implementation
*
* \returns The new library.
*/)")

		/// Member Variables

		/// Constructors

		/// Member Methods
		.def("add", py::overload_cast<double, double>(&CitePyExampleNS::IExample::add), R"(/*!
* \fn  virtual double IExample::add(double left, double right) = 0;
*
* \brief   Adds two doubles
*
* \param   left    The left.
* \param   right   The right.
*
* \returns the result.
*/)")
		.def("subtract", py::overload_cast<double, double>(&CitePyExampleNS::IExample::subtract), R"(/*!
* \fn  virtual double IExample::subtract(double left, double right) = 0;
*
* \brief   Subtracts two doubles
*
* \param   left    The left.
* \param   right   The right.
*
* \returns the result.
*/)")
		.def("compute", py::overload_cast<CitePyExampleNS::ExampleEnum, CitePyExampleNS::ExampleStruct>(&CitePyExampleNS::IExample::compute), R"(/*!
* \fn  virtual double IExample::compute(ExampleEnum option, ExampleStruct values) = 0;
*
* \brief   Computes
*
* \param   option  The option.
* \param   values  The values.
*
* \returns the result.
*/)")
	;

}