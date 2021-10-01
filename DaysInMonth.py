# File: DaysInMonth.py
# Student: Patty Chow
# UT EID: mpc2468
# Course Name: CS303E
# 
# Date Created: 02/15/2021
# Date Last Modified: 02/15/2021
# Description of Program: This program shows how many days each month has based on the month and year. This program also takes leap year into consideration and shows if February has 28 or 29 days based on the year.

#User input...
mth = int(input("Enter month (1-12): "))
yr = int(input("Enter year: "))

#assigning names to the number of the months...
if mth == 1: mth2 = "January"
elif mth == 2: mth2 = "February"
elif mth == 3: mth2 = "March"
elif mth == 4: mth2 = "April"
elif mth == 5: mth2 = "May"
elif mth == 6: mth2 = "June"
elif mth == 7: mth2 = "July"
elif mth == 8: mth2 = "August"
elif mth == 9: mth2 = "September"
elif mth == 10: mth2 = "October"
elif mth == 11: mth2 = "November"
elif mth == 12: mth2 = "December"
else: print("Please pick a month between 1 and 12.")

#assigning the number of days to months...
if mth == 1: day = "31"
elif mth == 3: day = "31"
elif mth == 4: day = "30"
elif mth == 5: day = "31"
elif mth == 6: day = "30"
elif mth == 7: day = "31"
elif mth == 8: day = "31"
elif mth == 9: day = "30"
elif mth == 10: day = "31"
elif mth == 11: day = "30"
elif mth == 12: day = "31"

#Leap year calculations for february ugh...
if mth2 == "February" and (yr % 400 == 0): day = "29"
elif mth2 == "February" and (yr % 100 == 0): day = "28"
elif mth2 == "February" and (yr % 4 == 0): day = "29"
elif mth2 == "February": day = "28"

#aaand the printing of the text...    
text = ("{} {} has {} days")
print(text.format(mth2, yr, day))