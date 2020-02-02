// mac937@nyu.edu
// Tandon CS Bridge Winter 2020
// Week 4
// Question 3
// Program that converts decimal to binary
// Note: behavior for negative integer inputs is undefined

#include <iostream>

using namespace std;

int main()
{
    int decimal;
    cout << "Enter decimal number:\n";
    cin >> decimal;

    int numBinaryDigits = 0;
    int intPart = decimal;
    do {
        intPart /= 2;
        numBinaryDigits++;
    } while (intPart > 0);

    cout << "The binary representation of " << decimal << " is ";
    for (int exponent = numBinaryDigits - 1; exponent >= 0; exponent--) {
        int powerOf2 = 1;
        for (int i = 0; i < exponent; i++) {
            powerOf2 *= 2;
        }
        if (decimal >= powerOf2) {
            cout << '1';
            decimal -= powerOf2;
        } else {
            cout << '0';
        }
    }
    cout << endl;
    return 0;
}
