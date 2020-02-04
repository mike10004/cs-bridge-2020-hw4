// mac937@nyu.edu
// Tandon CS Bridge Winter 2020
// Week 4
// Question 4
// Program that prints the geometric mean of a sequence of positive integers

// Note: behavior is undefined if the input sequence contains negative 
//       integers (in section (a)) or the product of the input integers 
//       is greater than what an int can store (in either section)

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    // Section (a)
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
    }

    cout << endl;

    // Section (b)
    {
        int sequenceLength = 0, sequenceElement;
        int product = 1;
        cout << "section b\n\n";
        cout << "Please enter a non-empty sequence of positive integers, each one on a \n"
                "separate line. End your sequence by typing -1:\n";
        do {
            cin >> sequenceElement;
            if (sequenceElement > 0) {
                product *= sequenceElement;
                sequenceLength++;
            }
        } while (sequenceElement > 0);

        double geometricMean = pow(product, 1.0 / sequenceLength);
        cout << "The geometric mean is: " << geometricMean << endl;
    }
    return 0;
}
