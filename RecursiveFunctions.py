# File: RecursiveFunctions.py
# Student: Patty Chow
# UT EID: mpc2468
# Course Name: CS303E
# 
# Date Created: 04/30/2021
# Date Last Modified: 04/30/2021
# Description of Program: This program uses recursive functions to solve a variety of problems shown below.

def sumItemsInList( L ):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList( L[1:] )
    #good!!

def countOccurrencesInList( key, L ):
    """ Return the number of times key occurs in 
    list L. """
    if L == []:
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList( key, L[1:] )
    else:
        return countOccurrencesInList( key, L[1:] )
    #good!!

def addToN ( n ):
    """ Add up the non-negative integers to n.
    E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5. """
    if n <= 0:
       return 0
    else:
        return n + addToN(n-1)
    #good!!

def findSumOfDigits( n ):
    """ Return the sum of the digits in a non-negative integer. """
    if n == 0:
       return 0
    else:
        return n % 10 + findSumOfDigits(n//10)
    #good!!

def decimalToBinary( n ):
    """ Given a nonnegative decimal integer n, return the 
    binary representation as a string. """
    if n <= 1:
       return str(n)
    
    else:
        quot = n//2
        rem = n % 2
        
        return decimalToBinary(quot) + str(rem)
        #good!!



def decimalToList( n ):
    """ Given a nonnegative decimal integer, return a list of the 
    digits (as strings). """
    if n < 0:
        return None
    elif 0 <= n < 10:
        return [str(n//1)]
    else:
        return decimalToList(n//10) + [str(n % 10)]
    #good!!
        


def isPalindrome( s ):
    """ Return True if string s is a palindrome and False
    otherwise. Count the empty string as a palindrome. """
    if s == "":
        return True
    elif len(s) == 1:
        return True
    else:
        if s[0] == s[-1]:
            return isPalindrome(s[1:-1])
        else:
            return False
        #good!!
        


def findFirstUppercase( s ):
    """ Return the first uppercase letter in 
    string s, if any.  Return None if there
    is none. """
    if s == "":
        return None
    elif s.islower():
        return None
    else:
        if 'A' <= s[0] <= 'Z':
            return s[0]
        else:
            return findFirstUppercase(s[1:])
        #good!!
    

def findFirstUppercaseIndexHelper( s, index ):
    """ Helper function for findFirstUppercaseIndex. """
    if s == "":
        return -1
    elif s.islower():
        return -1
    else:
        if 'A' <= s[0] <= 'Z':
            return index
        else:
            return findFirstUppercaseIndexHelper(s[1:], index+1)
        #GGGGOOOOODDD!!!!


# The following function is already completed for you.  But 
# make sure you understand what it's doing. 

def findFirstUppercaseIndex( s ):
    """ Return the index of the first uppercase letter in 
   string s, if any.  Return -1 if there is none.  This one 
   requires a helper function, which is the recursive 
   function. """
    return findFirstUppercaseIndexHelper( s, 0 )
