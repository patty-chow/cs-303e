# File: MinMax.py
# Student: Patty Chow
# UT EID: mpc2468
# Course Name: CS303E
# 
# Date Created: 02/23/2021
# Date Last Modified: 03/05/2021
# Description of Program: This program lets you input any integer, positive or negative, and figures out the maximum and minimum number of those inputs after you input "stop".

#idk what i'm doing....
#    ok mayybe..... 


#I first set this handy dandy variable in case the user replies 'stop' on the first go. I decided to put it before all the complicated stuff to not complicate it more.
noNum = "You didn't enter any numbers"

#In case the first input is stop I print noNum....
first_num = input("Enter an integer or 'stop' to end: ")
if first_num == "stop":
    print(noNum)

else:
#If not, I created a list out of the first input where the user could add onto until they type 'stop'.
        num_list = [first_num]

        while True:
            add_num = input("Enter an integer or 'stop' to end: ")
            num_list.append(add_num)

            if add_num != "stop":
                continue

#Once the user inputs stop, the loop stops, "stop" is removed from the list, and the max and min are found"
            else:
                num_list.remove("stop")
                print("The maximum is "+ max(num_list))
                print("The minimum is "+ min(num_list))

                break




