// mac937@nyu.edu
// Tandon CS Bridge Winter 2020
// Week 4
// Question 2
// Program that prints simplified Roman numerals

#include <iostream>

using namespace std;

const int VAL_M = 1000;
const int VAL_D = 500;
const int VAL_C = 100;
const int VAL_L = 50;
const int VAL_X = 10;
const int VAL_V = 5;
const int VAL_I = 1;

int main() {
    int decimal;
    cout << "Enter decimal number:\n";
    cin >> decimal;

    cout << decimal << " is ";
    char numeral = 'M';
    int chunkSize = VAL_M;
    while (decimal > 0) {
        if ((decimal - chunkSize) >= 0) {
            cout << numeral;
            decimal -= chunkSize;
        } else {
            switch (numeral) {
                case 'M':
                    numeral = 'D';
                    chunkSize = VAL_D;
                    break;
                case 'D':
                    numeral = 'C';
                    chunkSize = VAL_C;
                    break;
                case 'C':
                    numeral = 'L';
                    chunkSize = VAL_L;
                    break;
                case 'L':
                    numeral = 'X';
                    chunkSize = VAL_X;
                    break;
                case 'X':
                    numeral = 'V';
                    chunkSize = VAL_V;
                    break;
                case 'V':
                    numeral = 'I';
                    chunkSize = VAL_I;
                    break;
                default:
                    cerr << "numeral is " << numeral << "; this should be unreachable\n";
                    return 1;
            }
        }
    }
    cout << endl;
    return 0;
}
