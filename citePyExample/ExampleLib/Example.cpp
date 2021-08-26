#include "Example.h"
#include <numeric>

#define RETURN_WITH_CB(value) if(_cb) _cb(value); return value

namespace CitePyExampleNS
{
    ExampleStruct::ExampleStruct()
        : left(0.0),
          right(0.0) {}

    ExampleStruct::ExampleStruct(double left, double right)
        : left(left),
          right(right) {}

    double ExampleStruct::getLeft() const
    {
        return left;
    }

    std::unique_ptr<IExample> IExample::createLibrary()
    {
        return std::make_unique<Example>();
    }

    double Example::add(double left, double right) const
    {
        RETURN_WITH_CB(left + right);
    }

    double Example::subtract(double left, double right)
    {
        RETURN_WITH_CB(left - right);
    }

    double Example::compute(ExampleEnum option, ExampleStruct values)
    {
        switch (option)
        {
            case ExampleEnum::add: return add(values.left, values.right);
            case ExampleEnum::subtract: return subtract(values.left, values.right);
        }

        RETURN_WITH_CB(0.0);
    }

    double Example::compute(const std::vector<double>& values)
    {
        RETURN_WITH_CB(std::accumulate(values.begin(), values.end(), 0.0));
    }

    double Example::compute(SecondNamespace::ExternalStruct values)
    {
        return compute(values.listWithNumbersToAdd);
    }

    void Example::registerCallback(ExampleCallbackDefinition cb)
    {
        _cb = std::move(cb);
    }

    void Example::addReferenced(double& result, double left, double right)
    {
        result = add(left, right);
    }
}
