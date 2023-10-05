Exercise 1:

Write a program that reads the three edges of a triangle 
and computes the perimeter if the input is valid. 
The input is valid if the sum of every pair of two edges
is greater than the remaining edge. Otherwise (i.e. else) 
print a message stating that the input is invalid and 
the perimeter cannot be calculated.
(Note: This question does NOT require further input
validation.)


Example 1:

    Enter value for AB: 3
    Enter value for BC: 3
    Enter value for AC: 3

    output : Valid and the perimeter is 9

Example 2:

    Enter value for AB: 10
    Enter value for BC: 15
    Enter value for AC: 6

    output : Valid and the perimeter is 31

Example 3:

    Enter value for AB: 10
    Enter value for BC: 4
    Enter value for AC: 3

    output : Invalid

Code:

    x = int(input("Enter value for AB: "))
    y = int(input("Enter value for BC: "))
    z = int(input("Enter value for AC: "))

    (TODO)


