// Question 6
// Note: behavior is undefined for non-positive integers

#include <iostream>

using namespace std;

int BASE = 10;

int main()
{
    int positiveInt;
    cout << "Enter a positive integer: ";   
    cin >> positiveInt;
    for (int i = 0; i <= positiveInt; i++) {
        int numDigits = 0, numEvenDigits = 0, numOddDigits;
        int integerPart = i;
        while (integerPart > 0) {
            int remainder = integerPart % BASE;
            integerPart /= BASE;
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
