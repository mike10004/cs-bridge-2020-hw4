# Question 4

Write two versions of a program that reads a sequence of positive integers from 
the user, calculates their geometric mean, and prints the geometric mean.

Notes:

1. In mathematics, geometric mean of a set of n positive is the nth root of the 
   product of the numbers. For example, the geometric mean of 2, 9 and 12 is 
   equal to (2 ∙ 9 ∙ 12)^(1/3) = 6.
2. In order to calculate the n-th root of a number, you should call the `pow` 
   function, located in the `cmath` library.

Your two versions should read the integer sequence in two ways:

a) First read the length of the sequence.

For example, an execution would look like:

    Please enter the length of the sequence: 3
    Please enter your sequence:
    1
    2
    3
    The geometric mean is: 1.8171

b) Keep reading the numbers until -1 is entered.

For example, an execution would look like:

    Please enter a non-empty sequence of positive integers, each one in a separate line. End your
    sequence by typing -1:
    1
    2
    3
    -1
    The geometric mean is: 1.8171
