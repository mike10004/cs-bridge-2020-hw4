// Question 3
// Behavior for negative integers is undefined

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
