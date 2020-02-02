// mac937@nyu.edu
// Tandon CS Bridge Winter 2020
// Week 4
// Question 5
// Program that prints an asterisk hourglass

#include <iostream>

using namespace std;

int main()
{
    int hourglassHalfHeight;
    cout << "Enter a positive integer: ";
    cin >> hourglassHalfHeight;
    for (int row = hourglassHalfHeight - 1; row >= 0; row--) {
        for (int col = 0; col < (hourglassHalfHeight - row - 1); col++) {
            cout << ' ';
        }
        for (int star = 0; star < (row * 2 + 1); star++) {
            cout << '*';
        }
        cout << endl;
    }
    for (int row = 0; row < hourglassHalfHeight; row++) {
        for (int col = 0; col < (hourglassHalfHeight - row - 1); col++) {
            cout << ' ';
        }
        for (int star = 0; star < (row * 2 + 1); star++) {
            cout << '*';
        }
        cout << endl;
    }
    return 0;
}
