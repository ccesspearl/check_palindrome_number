# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

# original number 121
# Yes. given number is palindrome number

# original number 125
# No. given number is not palindrome number

# Pseudocode 

# Create a checking function for the given number 
def checking(number):

# Inside the function, create a variable that will convert the number to string 
    given_number = str(number)

# Inside the function, create a variable that will reverse the given number string 
    new_number = given_number[::-1]
    
# Inside the function, use if statement to know whether the number and its reverse is palindrome 
# Inside the function, use else statement to print whether the number and its reverse is not palindrome 
# Check the numbers and print the result 