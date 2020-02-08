// mac937@nyu.edu
// Tandon CS Bridge Winter 2020
// Week 4
// Question 3
// Program that converts decimal to binary
// Note: behavior for negative integer inputs is undefined

#include <iostream>

using namespace std;

int main() {
    int decimal;
    cout << "Enter decimal number:\n";
    cin >> decimal;

    // Find the greatest power of 2 less than or equal to the input number
    int powerOf2 = 1;
    while ((powerOf2 * 2) <= decimal) {
        powerOf2 *= 2;
    }
    
    cout << "The binary representation of " << decimal << " is ";
    while (powerOf2 > 0) {
        if (decimal >= powerOf2) {
            cout << '1';
            decimal -= powerOf2;
        } else {
            cout << '0';
        }
        powerOf2 /= 2;
    }
    cout << endl;
    return 0;
}
