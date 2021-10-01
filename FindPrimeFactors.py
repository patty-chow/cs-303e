# File: FindPrimeFactors.py
# Student: Patty Chow
# UT EID: mpc2468
# Course Name: CS303E
# 
# Date Created: 04/07/2021
# Date Last Modified: 04/09/2021
# Description of Program: This program finds the prime factorization of a number. However, if the number inputted is 0, 1, or negative, the program will let them know so.


import math
numList=[]

def isPrime(num):
    if(num<2 or num%2 == 0):
        return (num == 2)
    divisor = 3
    while(divisor<=math.sqrt(num)):
        if(num%divisor == 0):
            return False
        else:
            divisor += 2
    return True

def findNextPrime(num):
    if (num<2):
        return 2
    if(num%2 == 0):
        num -= 1
    guess= num+2
    while(not isPrime(guess)):
        guess += 2
    return guess
    

print("Find Prime Factors:")

while True:
    num = int(input("Enter a positive integer (or 0 to stop): "))
    
    if(num == 1):
        print("  1 has no prime factorization.")
        print()
    elif(num == 0):
        print("Goodbye!")
        break
    elif(num < 0):
        print("  Negative integer entered.  Try again.")
        print()
    else:
        if(isPrime(num) == True):
            numList.clear()
            numList.append(num)
            print("  The prime factorization of "+str(num)+" is:", numList)
            print()
        else:
            numList.clear()
            inputNum= num
            divisor = 2
            while(num > 1):
                if(num%divisor == 0):
                    numList.append(divisor)
                    num = num/divisor
                else:
                    divisor = findNextPrime(divisor)
            print("  The prime factorization of "+str(inputNum)+" is:", numList)
            print()

