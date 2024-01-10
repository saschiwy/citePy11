#include <iostream>
#include "MyInteger.h"

MyInteger::MyInteger(): value(0)
{
}

MyInteger::MyInteger(int v): value(v)
{
}

MyInteger::operator int() const
{
    return value;
}

MyInteger MyInteger::operator+(const MyInteger& other) const
{
    return MyInteger(value + other.value);
}

MyInteger MyInteger::operator-(const MyInteger& other) const
{
    return MyInteger(value - other.value);
}

MyInteger MyInteger::operator*(const MyInteger& other) const
{
    return MyInteger(value * other.value);
}

MyInteger MyInteger::operator/(const MyInteger& other) const
{
    if (other.value == 0)
    {
        std::cerr << "Division by zero!\n";
        return MyInteger();
    }
    return MyInteger(value / other.value);
}

bool MyInteger::operator==(const MyInteger& other) const
{
    return value == other.value;
}

bool MyInteger::operator!=(const MyInteger& other) const
{
    return !(*this == other);
}

bool MyInteger::operator<(const MyInteger& other) const
{
    return value < other.value;
}

bool MyInteger::operator<=(const MyInteger& other) const
{
    return value <= other.value;
}

bool MyInteger::operator>(const MyInteger& other) const
{
    return value > other.value;
}

bool MyInteger::operator>=(const MyInteger& other) const
{
    return value >= other.value;
}

MyInteger& MyInteger::operator++()
{
    ++value;
    return *this;
}

MyInteger& MyInteger::operator--()
{
    --value;
    return *this;
}

int MyInteger::getValue() const
{
    return value;
}

MyInteger MyInteger::add(MyInteger a, MyInteger b)
{
    return MyInteger(a.getValue() + b.getValue());
}

std::ostream& operator<<(std::ostream& os, const MyInteger& myInt)
{
    os << myInt.value;
    return os;
}

MyInteger MyInteger::operator+(const int& other) const
{
    return MyInteger(value + other);
}

MyInteger MyInteger::operator-(const int& other) const
{
    return MyInteger(value - other);
}

MyInteger MyInteger::operator*(const int& other) const
{
    return MyInteger(value * other);
}

MyInteger MyInteger::operator/(const int& other) const
{
    return MyInteger(value / other);
}

bool MyInteger::operator==(const int& other) const
{
    return value == other;
}

bool MyInteger::operator!=(const int& other) const
{
    return value != other;
}

bool MyInteger::operator<(const int& other) const
{
    return value < other;
}

bool MyInteger::operator<=(const int& other) const
{
    return value <= other;
}

bool MyInteger::operator>(const int& other) const
{
    return value > other;
}

bool MyInteger::operator>=(const int& other) const
{
    return value >= other;
}
