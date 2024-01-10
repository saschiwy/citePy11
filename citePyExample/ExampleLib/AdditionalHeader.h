#pragma once
#include <vector>

// Create a second Header without comments.

namespace SecondNamespace
{
    struct ExternalStruct
    {
        enum class Test
        {
            a,
            b
        };

        Test testEnum{};
        double exampleDouble{};

        std::vector<double> listWithNumbersToAdd{};
    };
}
