//
// Created by sasc on 10.01.24.
//

#ifndef ADDITIONALHEADER2_H
#define ADDITIONALHEADER2_H

#include "AdditionalHeader.h"

namespace SecondNamespace
{
    struct ExternalStruct2
    {
        ExternalStruct::Test testEnum{};
    };
}

namespace four::namespaces::at::once
{
    struct ExternalStruct3
    {
        int testInt{};

        /**
         * @brief Set the testInt value
         *
         * @param value
         * @return int
         */
        int setTestInt(int value)
        {
            testInt = value;
            return testInt;
        }
    };
}
#endif //ADDITIONALHEADER2_H
