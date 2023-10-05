# Exercise 1:

Write a program that reads the three edges of a triangle 
and computes the perimeter if the input is valid. 
The input is valid if the sum of every pair of two edges
is greater than the remaining edge. Otherwise (i.e. else) 
print a message stating that the input is invalid and 
the perimeter cannot be calculated.
(Note: This question does NOT require further input
validation.)


Case 1:

    Enter value for AB: 3
    Enter value for BC: 3
    Enter value for AC: 3

    output : Valid and the perimeter is 9

Case 2:

    Enter value for AB: 10
    Enter value for BC: 15
    Enter value for AC: 6

    output : Valid and the perimeter is 31

Case 3:

    Enter value for AB: 10
    Enter value for BC: 4
    Enter value for AC: 3

    output : Invalid

Code:

    x = int(input("Enter value for AB: "))
    y = int(input("Enter value for BC: "))
    z = int(input("Enter value for AC: "))

    (TODO)


# Exercise 2:

Create a bill split program and a tip calculator, taking 3 user inputs, the bill amount (in dollars), the % of the bill for the tip that's going to be given, and
the amount of people. the program should output the total amount per person should pay, and the tip amount per person


Case 1:

    Enter amount of bill: 100
    Enter number of people: 5
    Enter amount of tip(%): 10

    Tip amount per person $2.00
    Total amount per person $22.00

    (100/5) = 20
    Tip total = 10% x 100 = 10; 10/5 = 2
    Per person total = 20+2 = 22

Case 2:

    Enter amount of bill: 503
    Enter number of people: 3
    Enter amount of tip(%): 5

    Tip amount per person $8.38
    Total amount per person $176.05

Case 3:

    Enter amount of bill: 77
    Enter number of people: 10
    Enter amount of tip(%): 2

    Tip amount per person $0.15
    Total amount per person $7.85

Code:

    bill = float(input("Enter amount of bill: "))
    num_of_people = int(input("Enter number of people: "))
    tip = float(input("Enter amount of tip (%): "))

    (TODO)


# Exercise 3:

Create a program that translate a certain amount of seconds and format it to world time format (0:0:0). The program will take an integer as input
that represents the amount of seconds and will be converted to the world time format.


Case 1:

    Enter the number of seconds: 3600
    Results: 1:0:0

Case 2:

    Enter the number of seconds: 12345
    Results: 3:25:45

Case 3:

    Enter the number of seconds: 777
    Results: 0:12:57

Code:

    time = int(input("Enter the number of seconds: "))

    (TODO)


# Exercise 4:

Given a list as below, concatenate each element of the list with its corresponding element from the other list.

Code:

    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]
    (TODO)

    output: ['My', 'name', 'is', 'Kelly']


# Exercise 5:

Given a list as below, concatenate each element of the list with its corresponding opposite element from the other list.

Code:

    list1 = [10,20,30,40]
    list2 = [100,200,300,400]
    (TODO)

    output: 

    10 400
    20 300
    30 200
    40 100

# Exercise 6:

Given a list as below, concatenate each element of the list with all of the other list's elements

Code:

    list1 = ["Hello", "take"]
    list2 = ["Dear", "Sir"]
    (TODO)

    output: 

    ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
