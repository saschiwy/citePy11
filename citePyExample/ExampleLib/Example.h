#ifndef EXAMPLE_H
#define EXAMPLE_H
#include "IExample.h"

namespace CitePyExampleNS
{
    class Example : public IExample
    {
    public:
        double add(double left, double right) override;

        double subtract(double left, double right) override;

        double compute(ExampleEnum option, ExampleStruct values) override;
    };
}
#endif // EXAMPLE_H
