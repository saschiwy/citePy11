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

        double compute(const std::vector<double>& values) override;

        double compute(SecondNamespace::ExternalStruct values) override;

        void registerCallback(ExampleCallbackDefinition cb) override;

        void addReferenced(double& result, double left, double right) override;

    private:
        ExampleCallbackDefinition _cb{nullptr};
    };
}
#endif // EXAMPLE_H
