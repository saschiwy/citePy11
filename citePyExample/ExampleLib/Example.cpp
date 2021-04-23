#include "Example.h"

namespace CitePyExampleNS
{
    ExampleStruct::ExampleStruct()
        : left(0.0),
          right(0.0) {}

    ExampleStruct::ExampleStruct(double left, double right)
        : left(left),
          right(right) {}

    std::unique_ptr<IExample> IExample::createLibrary()
    {
        return std::make_unique<Example>();
    }

    double Example::add(double left, double right)
    {
        return left + right;
    }

    double Example::subtract(double left, double right)
    {
        return left - right;
    }

    double Example::compute(ExampleEnum option, ExampleStruct values)
    {
        switch (option)
        {
            case ExampleEnum::add: return add(values.left, values.right);
            case ExampleEnum::subtract: return subtract(values.left, values.right);
        }

        return 0.0;
    }
}
