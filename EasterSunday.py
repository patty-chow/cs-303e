# File: EasterSunday.py
# Student: Patty Chow
# UT EID: mpc2468
# Course Name: CS303E
#
# Date Created: 01/24/2021
# Date Last Modified: 01/27/2021
# Description of Program: This program computes the date of Easter Sunday given any year.

y = int(input("Enter year: "))

#math to figure out month and day of Easter Sunday
#learn how to indent correctly to improve formatting
a = y % 19
b = y//100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b - d - g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m + 32) % 7
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32

#Printing the statement.
#is this how to format it right? think so.
#is this how Prof. Young wants us to format it? We have to wait.
text = ("In {} Easter Sunday is on month {} and day {}.")
print(text.format(y, n, p))
