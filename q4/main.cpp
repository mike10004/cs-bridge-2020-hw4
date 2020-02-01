// Question 4

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int sequenceLength, sequenceElement;
    int product = 1;
    cout << "section a\n\n";
    cout << "Please enter the length of the sequence: ";
    cin >> sequenceLength;
    cout << "Please enter your sequence:\n";
    for (int i = 0; i < sequenceLength; i++) {
        cin >> sequenceElement;
        product *= sequenceElement;
    }
    double geometricMean = pow(product, 1.0 / sequenceLength);
    cout << "The geometric mean is: " << geometricMean << endl;
    cout << "\nsection b\n\n";
    product = 1;
    sequenceLength = 0;
    cout << "Please enter a non-empty sequence of positive integers, each one in a \n"
            "separate line. End your sequence by typing -1:\n";
    do { 
        cin >> sequenceElement;
        if (sequenceElement > 0) {
            product *= sequenceElement;
            sequenceLength++;
        }
    } while (sequenceElement > 0);
    geometricMean = pow(product, 1.0 / sequenceLength);
    cout << "The geometric mean is: " << geometricMean << endl;
    return 0;
}
