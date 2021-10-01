# File: CalculatePI.py
# Student: Patty Chow
# UT EID: mpc2468
# Course Name: CS303E
# Unique Number: 52090
# 
# Date Created: 03/14/2021 (HAPPY PI DAY!!!)
# Date Last Modified: 03/15/2021
# Description of Program: 

import math
import random

hitList = 0

#learn more about functions. why would i need one?
#def computePI ( numThrows ):
numThrows = int(input("Insert number of throws: "))
for x in range (0, numThrows):
    xPos = random.uniform (-1.0, 1.0)
    yPos = random.uniform (-1.0, 1.0)
    hypo = math.hypot(xPos, yPos)
    if hypo <= 1:
        hitList += 1

numThrowsString = format(numThrows)
numThrowsString2 = format(numThrowsString, "11s")

calc = 4 * (hitList/numThrows)
calcString = format(calc,".6f")

diff = calc - math.pi
diffString = format(diff, ".6f")

if diff == 0:
    sign = None
elif diff < 0:
    sign = "-"
else:
    sign = "+"

print("num = " + numThrowsString2 + "Calculated PI = " + calcString + "   Difference = " + sign + diffString)
#QUESTIONS
#   1. what is the function of a function?
#   2. how do i make it work?
#   3. why do i need 2 functions in my work?