// mac937@nyu.edu
// Tandon CS Bridge Winter 2020
// Week 4
// Question 6
// Program that prints numbers with more even digits than odd digits 

#include <iostream>

using namespace std;

int DECIMAL_BASE = 10;

int main()
{
    int positiveInt;
    cout << "Enter a positive integer: ";   
    cin >> positiveInt;
    for (int i = 0; i <= positiveInt; i++) {
        int numDigits = 0, numEvenDigits = 0, numOddDigits;
        int integerPart = i;
        while (integerPart > 0) {
            int remainder = integerPart % DECIMAL_BASE;
            integerPart /= DECIMAL_BASE;
            if ((remainder % 2) == 0) {
                numEvenDigits++;
            }
            numDigits++;
        }
        numOddDigits = numDigits - numEvenDigits;
        if (numEvenDigits > numOddDigits) {
            cout << i << endl;
        }
    }
    return 0;
}
