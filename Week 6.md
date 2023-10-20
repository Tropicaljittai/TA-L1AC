## Problem 1:
When a person receives a blood transfusion, it is essential to make sure that the donor's blood type is
compatible with the receiver's blood type. Receiving a blood type that is not compatible with your own can be life-threating, so blood banks always make sure
to note the type of blood they receive from donors so that they can ensure a safe transfusion Blood types are named according to three factors presence of antigen A, presence of antigen B, and
presence of Rh factor. If antigen A is found, the blood type includes the letter "A". If antigen B is found, the blood type includes the letter "B". And if the Rh factor
is present, the blood type ends with "+"; otherwise, it ends with "-". If neither antigen A nor antigen B are found, the blood type includes the letter "0" For example, a person with only antigen A would have
the blood type "A-". A person with both antigens A and B and the Rh factor would have blood type "AB+ and a person wih only the Rh factor would have blood type "0+"

## The rules for giving and receiving blood are as follows:
A person with antigen A may only give blood to another person with antigen A.

A person with antigen B may only give blood to another person with antigen B.

A person with the Rh factor may only give blood to another person with the Rh factor.

A person with none of the above factors (0-) can give blood to anyone.

Write a function that takes in a donor's and receiver's blood types as strings and returns whether or not the donor can safely give blood to the receiver, 
according to the rules above

## Examples
canGiveBlood("0+", "A+") -> true

canGiveBlood("A-", "B-") -> false

canGiveBlood("A-", "AB+") -> true

**Notes**

All letters are capital.

Each blood type will be one of the following strings: "O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"

## Problem 2:
In Digital Decipher, decoding is done by the
simple subtraction of numbers in the key and the
corresponding characters on a given array. You
may want to solve this challenge before proceeding
further.

Create a function that takes two arguments; a
positive integer and an array of integers and returns a
decoded message as string
Assign a unique number to each letter of the
alphabet.

a b c d e f g h i j k l m n o p q r s t u v w x y z

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
22 23 24 25 26

There are some variations on the rules of
encipherment. One version of the cipher rules are
outlined below:

eMessage = [20, 12, 18, 30, 21]
, key = 1939

digitalDecipher(eMessage, key) > "scout"

Subtract each key digit from eMessage consecutive
digits:

20 12 18 30 21

-1       9  3  9  1

______________ -

19 3 15 21 20

Write the corresponding number against each
character:

s c o u t

19 3 15 21 20

See the below example for a better understanding:

eMessage = [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]

key = 1939

digitalDecipher(eMessage, key) - "masterpiece

14 10 22 29 6 27 19 18 6 12 8

-1  9  3  9  1  9  3  9  1  9  3

________________________________ -

13  1  19  20  5  18  16  9  5  3  5

m a s t e r p i e c e

Examples

digitalDecipher([20, 12, 18, 30, 21], 1939) -> "scout"

digitalDecipher([14, 30, 11, 1, 20, 17, 18, 18], 1990)-4
"mubashir"

digitalDecipher([6, 4, 1, 3, 9, 20], 100) -> "edabit"
