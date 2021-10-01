# File: Benford.py
# Student: Patty Chow
# UT EID: mpc2468
# Course Name: CS303E
# 
# Date Created: 04/21/2021
# Date Last Modified: 04/23/2021
# Description of Program: This program proves Benford's Law in 2009 Census data. In order for it to be proven, 1 should be the leading number with the highest persentage.

import os.path

#accepting the name of a file....
file = input("Enter the name of a file of census data: ")
if not os.path.exists(file):
    print("File does not exist")
    exit
else:
    digitPop = {}
    with open(file, 'r') as read_file:
        lines = read_file.readlines()[1:]
        for line in lines:
            line = line.strip()
            if len(line) == 0:
                continue
            else:
                line = line.split()
                digitOne = int(line[-1][0])
                if digitPop.get(digitOne) == None:
                    digitPop[digitOne] = int(line[-1])
                else:
                   digitPop[digitOne] = int(line[-1]) + digitPop.get(digitOne)


    totalPop = sum(digitPop.values())
    print('{:5}{:>12}{:>8}'.format('Digit', 'Count', 'Percentage'))
    for i in range (1,10):
        if digitPop.get(i) == None:
            population = 0
        else:
            population = digitPop.get(i)
        print('{:<5}{:>12}{:>8.1f}'.format(i, population, 100 * population / totalPop))
