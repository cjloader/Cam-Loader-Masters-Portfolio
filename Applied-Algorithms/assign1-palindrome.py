#!/usr/bin/env python3

def isPalindrome(phrase):
    # Take in the input and cast it to str
    stringToCheck = (str)(phrase)
    # Measure how long the input string is
    phraseSize = len(stringToCheck)
    ##Check if phrase is bigger than 0, 1 respectively
    if (phraseSize == 0): # if 0 - fail
       return False
    if (phraseSize == 1): #if 1 - pass
       return True
    if (phraseSize == 2):
        return (stringToCheck[0].casefold() == stringToCheck[-1].casefold())
    elif (phraseSize > 1):
        ## If greater than 1, recursively check the substring
        if (stringToCheck[0].casefold() == stringToCheck[-1].casefold()):
           return isPalindrome(stringToCheck[+1:-1].casefold())
        else:
           return False
    else:
        return False


greet = True
## Start of the program it prompts for input until it gets a Q
while(greet):
    phrase = input("Enter a string to check for palindrome. Q to exit: ")
    if phrase ==  "Q":
        greet = False
        exit(1)
## If not Q it proceeds to check for palindrome
    if isPalindrome(phrase):
        print(phrase+ " is a palindrome.")
    else:
        print(phrase+ " is not a palindrome.")
