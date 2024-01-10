//
// Created by sasc on 10.01.24.
//

#ifndef MYINTEGER_H
#define MYINTEGER_H

class MyInteger
{
private:
    int value;

public:
    // Constructors
    MyInteger();

    explicit MyInteger(int v);

    // Conversion operator to int
    explicit operator int() const;

    // Binary arithmetic operators
    MyInteger operator+(const MyInteger& other) const;

    MyInteger operator-(const MyInteger& other) const;

    MyInteger operator*(const MyInteger& other) const;

    MyInteger operator/(const MyInteger& other) const;

    // Relational operators
    bool operator==(const MyInteger& other) const;

    bool operator!=(const MyInteger& other) const;

    bool operator<(const MyInteger& other) const;

    bool operator<=(const MyInteger& other) const;

    bool operator>(const MyInteger& other) const;

    bool operator>=(const MyInteger& other) const;

    MyInteger operator+(const int& other) const;

    MyInteger operator-(const int& other) const;

    MyInteger operator*(const int& other) const;

    MyInteger operator/(const int& other) const;

    // Relational operators
    bool operator==(const int& other) const;

    bool operator!=(const int& other) const;

    bool operator<(const int& other) const;

    bool operator<=(const int& other) const;

    bool operator>(const int& other) const;

    bool operator>=(const int& other) const;

    // Increment and decrement operators
    MyInteger& operator++();

    MyInteger& operator--();

    // Additional functions
    int getValue() const;

    // Friend function to overload the << operator for easy printing
    friend std::ostream& operator<<(std::ostream& os, const MyInteger& myInt);

    static MyInteger add(MyInteger a, MyInteger b);
};


#endif //MYINTEGER_H
