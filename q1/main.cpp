// mac937@nyu.edu
// Tandon CS Bridge Winter 2020
// Week 4
// Question 1

#include <iostream>

using namespace std;

int main()
{
    int numEvenNumbersToPrint;
    cout << "Please enter a positive integer: ";
    cin >> numEvenNumbersToPrint;

    cout << "section a" << endl;
    int printedNumberCount = 0;
    while (printedNumberCount < numEvenNumbersToPrint)
    {
        cout << (2 * (printedNumberCount + 1)) << endl;
        printedNumberCount++;
    }

    cout << "section b" << endl;
    for (int i = 0; i < numEvenNumbersToPrint; i++)
    {
        cout << (2 * (i + 1)) << endl;
    }

    return 0;
}
