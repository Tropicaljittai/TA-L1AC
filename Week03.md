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

    # Taking user input and initializing an empty list that will be used to form the new string
    
    camelcase = input("String: ")
    snakecase = []

    # Loop thru each character in the string, while looking for an uppercase letter, when it finds one add "_" + the letter that was found. Other than that add the character itself to the list
    
    for i in camelcase:
        if i.isupper():
            snakecase.append('_'+i)
        else:
            snakecase.append(i)

    # Transform the list into a string
    
    final = ''.join(snakecase)

    # Print out the string, and lowercase the string
    
    print(final.lower())


Exercise 2

The program takes input some amount of change (in dollars) & the program will subtract by the biggest posssible amount (¢1, ¢5, ¢10, ¢25) until there is 0 change left and return how many coins needed to reach 0.

example:

    change owed: 0.41
    output: 4
        (41 - 25 = 16 , 16 - 10 = 6, 6 - 5 = 1, 1 - 1 = 0)
            1 coin    +   1 coin  +   1 coin  +   1 coin    = 4 coins
        
    change owed: 1.60
    output: 7
        
    change owed: 4.2
    output: 18

Solution 2:

    # Keep prompting the user for input until a valid answer is given and cast it into a float
    
    while True:
        change = float(input("Change owed: "))
        if change > 0:
            break

    # Multiply the input by 100 to make it easier when performing the operations
    
    coins = change * 100
    count = 0

    # While the original change owed is not 0, subtract it with 25 if it's bigger or equal to 25, and goes the same for 10, 5, and 1 cents. With every subtraction add 1 coin count to the variable 'count'
    
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

    # Print out how many coins that was counted thru each subtraction
    
    print(count)


Exercise 3:

Create a program that detects wether a string is eligible to be a vanity plate or not. 

Vanity plates must start with at least two characters, maximum of 6 characters (letter and number), and a minimum of 2 characters. 

There can't be a number inbetween letters. 

The numbers must be at the end. 

For example, AAA222 would be an acceptable vanity plate. AAA22A would not be acceptable. 

The first number used cannot be a '0' and the string must only consist of letters and numbers.

Submit here: https://forms.gle/Sq38fPWHrLWAQn6f9

example:

    Plate : TA11
    output: valid
        
    Plate: 11TA
    output: invalid
    
    Plate: TA1A
    output: invalid

OPTIONAL ASSIGNMENT (pick 1 out of these 2):

Variation 1:

Using loops, create a program that prints out a pattern of half a pyramid as seen below:
The program must take only integers as an input and that integer must be in the range of 1 until 8, other than that keep prompting the user for another input.
Submit thru here: https://forms.gle/KXQcuMmnWEtgFya9A

    Height: 8
    
           #
          ##
         ###
        ####
       #####
      ######
     #######
    ######## 

Variation 2:

Using loops, create a program that prints out a pattern of a full pyramid as seen below:
The program must take only integers as an input and that integer must be in the range of 1 until 8, other than that keep prompting the user for another input.
Submit thru here: https://forms.gle/KXQcuMmnWEtgFya9A

    Height: 8
   
           #  #
          ##  ##
         ###  ###
        ####  ####
       #####  #####
      ######  ######
     #######  #######
    ########  ########
