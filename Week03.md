Exercise 1:

Make a program that turns a string from this "snakeCase" to this "snake_case"

example:

    String: testCaseLetter
    output: test_case_letter
        
    String: testCase
    output: test_case
    
    String: test
    output: test
    
Solution 1:

    camelcase = input("String: ")
    snakecase = []
    
    for i in camelcase:
        if i.isupper():
            snakecase.append('_'+i.lower())
        else:
            snakecase.append(i)
    
    final = ''.join(snakecase)
    
    print(final.lower())


Exercise 2

The program takes input some amount of change (in dollars) & the program will subtract by the biggest posssible amount (¢1, ¢5, ¢10, ¢25) until there is 0 change left and return how many coins needed to reach 0.

example:

    change owed: 0.41
    output: 4
        (41 - 25 = 16 , 16 - 10 = 6, 6 - 5 = 1, 1 - 1 = 0)
        
    change owed: 1.60
    output: 7
        
    change owed: 4.2
    output: 18

Solution 2:

    while True:
        change = float(input("Change owed: "))
        if change > 0:
            break
    
    coins = change * 100
    count = 0
    
    while coins > 0:
        if coins >= 25:
            coins -= 25
            count += 1
        elif coins >= 10:
            coins -= 10
            count += 1
        elif coins >= 5:
            coins -= 5
            count += 1
        else:
            coins -= 1
            count += 1
    
    print(count)


Exercise 3:

Create a program that detects wether a string is eligible to be a vanity plate or not. 

Vanity plates must start with at least two characters, maximum of 6 characters (letter and number), and a minimum of 2 characters. 

There can't be a number inbetween letters. 

The numbers must be at the end. 

For example, AAA222 would be an acceptable vanity plate. AAA22A would not be acceptable. 

The first number used cannot be a '0' and the string must only consist of letters and numbers.

example:

    Plate : TA11
    output: valid
        
    Plate: 11TA
    output: invalid
    
    Plate: TA1A
    output: invalid
        
        
        
        
        
        
        
