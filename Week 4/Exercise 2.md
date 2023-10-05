Exercise 2:

Create a bill split program and a tip calculator, taking 3 user inputs, the bill amount (in dollars), the % of the bill for the tip that's going to be given, and
the amount of people. the program should output the total amount per person should pay, and the tip amount per person


Example 1:

    Enter amount of bill: 100
    Enter number of people: 5
    Enter amount of tip(%): 10

    Tip amount per person $2.00
    Total amount per person $22.00

    (100/5) = 20
    Tip total = 10% x 100 = 10; 10/5 = 2
    Per person total = 20+2 = 22

Example 2:

    Enter amount of bill: 503
    Enter number of people: 3
    Enter amount of tip(%): 5

    Tip amount per person $8.38
    Total amount per person $176.05

Example 3:

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


