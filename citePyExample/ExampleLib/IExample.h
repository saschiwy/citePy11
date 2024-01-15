#pragma once

#include <functional>
#include <memory>

#include "AdditionalHeader.h"

/*!
 * \namespace   CitePyExampleNS
 *
 * \brief   The example Namespace.
 */
namespace CitePyExampleNS
{
    typedef double SomeUselessTypeDef;

    /*!
     * \enum    ExampleEnum
     *
     * \brief   Values that represent example enums
     */
    enum ExampleEnum
    {
        add,     ///< An enum constant representing the add option
        subtract ///< An enum constant representing the subtract option
    };

    /*!
     * \struct  ExampleStruct
     *
     * \brief   An example structure.
     */
    struct ExampleStruct
    {
        double left;  ///< The left
        double right; ///< The right

        /*!
         * \fn  ExampleStruct();
         *
         * \brief   Default constructor
         */
        ExampleStruct();

        /*!
         * \fn  ExampleStruct(double left, double right);
         *
         * \brief   Constructor
         *
         * \param   left    The left.
         * \param   right   The right.
         */
        ExampleStruct(double left, double right);

        template <typename T> void set(T val1, T val2)
        {
            left  = static_cast<double>(val1);
            right = static_cast<double>(val2);
        }

        double getLeft() const;
    };

    /*!
     * \class   IExample
     *
     * \brief   An example class to show the usage ot citePy
     */
    class IExample
    {
    public:
        /*!
         * \typedef std::function<void(double)> ExampleCallbackDefinition
         *
         * \brief   Defines an alias representing the example callback definition
         */
        typedef std::function<void(double)> ExampleCallbackDefinition;

        virtual ~IExample() = default;

        /*!
         * \fn  static std::unique_ptr<IExample> IExample::createLibrary();
         *
         * \brief   Instantiates a library object without knowledge about the implementation
         *
         * \returns The new library.
         */
        static std::unique_ptr<IExample> createLibrary();

        /*!
         * \fn  virtual double IExample::add(double left, double right) = 0;
         *
         * \brief   Adds two doubles
         *
         * \param   left    The left.
         * \param   right   The right.
         *
         * \returns the result.
         */
        virtual double add(double left, double right) const = 0;

        /*!
         * \fn  virtual double IExample::subtract(double left, double right) = 0;
         *
         * \brief   Subtracts two doubles
         *
         * \param   left    The left.
         * \param   right   The right.
         *
         * \returns the result.
         */
        virtual double subtract(double left, double right) = 0;

        /*!
         * \fn  virtual double IExample::compute(ExampleEnum option, ExampleStruct values) = 0;
         *
         * \brief   Computes with an enum operator and the values inside the example structure
         *
         * \param   option  The option.
         * \param   values  The values.
         *
         * \returns the result.
         */
        virtual double compute(ExampleEnum option, ExampleStruct values) = 0;

        /*!
         * \fn  virtual double IExample::compute(SecondNamespace::ExternalStruct values) = 0;
         *
         * \brief   Adds all the given values, inside the vector
         *
         * \param   values  The values.
         *
         * \returns A double.
         */
        virtual double compute(const std::vector<double>& values) = 0;

        /*!
         * \fn  virtual double IExample::compute(SecondNamespace::ExternalStruct values) = 0;
         *
         * \brief   Computes the given values
         *
         * \param   values  The values.
         *
         * \returns A double.
         */
        virtual double compute(SecondNamespace::ExternalStruct values) = 0;

        /*!
         * \fn  virtual void IExample::registerCallback(ExampleCallbackDefinition cb) = 0;
         *
         * \brief   Registers the callback described by cb
         *
         * \param   cb  The cb.
         */
        virtual void registerCallback(ExampleCallbackDefinition cb) = 0;

        /*!
         * \fn  virtual void IExample::addReferenced(double& result, double left, double right) = 0;
         *
         * \brief   Adds a referenced
         *
         * \param [in,out]  result  The result.
         * \param           left    The left.
         * \param           right   The right.
         */
        virtual void addReferenced(double& result, double left, double right) = 0;
    };
}
