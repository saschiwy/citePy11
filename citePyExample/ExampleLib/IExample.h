#ifndef IEXAMPLE_H
#define IEXAMPLE_H
#include <memory>

/*!
 * \namespace   CitePyExampleNS
 *
 * \brief   The example Namespace.
 */
namespace CitePyExampleNS
{
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
        virtual double add(double left, double right) = 0;

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
         * \brief   Computes
         *
         * \param   option  The option.
         * \param   values  The values.
         *
         * \returns the result.
         */
        virtual double compute(ExampleEnum option, ExampleStruct values) = 0;
    };
}

#endif // IEXAMPLE_H
