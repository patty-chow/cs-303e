# File: Student.py
# Student: Patty Chow
# UT EID: mpc2468
# Course Name: CS303E
# 
# Date Created: 03/24/2021
# Date Last Modified: 03/26/2021
# Description of Program: This program records a student's exam grades and exam average by having the user input a student's names and grades. This program may also cure cancer. Who knows?

class Student:

#defining the variables we're gonna use.
    def __init__(self, name = None, exam1 = None, exam2 = None):
        self.__name = name
        self.__exam1 = exam1
        self.__exam2 = exam2

#what the final output will look like when the user inputs print(). I want to know why it does so.
    def __str__(self):
        return "Student: " + str(self.__name) + "\n  Exam1: " + str(self.__exam1) + "\n  Exam2: " + str(self.__exam2)

#recording of inputs (set) and output of those inputs (get)    
    def getName(self):
        return self.__name
    
    def setExam1Grade(self, exam1):
        self.__exam1 = exam1

    def getExam1Grade(self):
        return self.__exam1

    def setExam2Grade(self, exam2):
        self.__exam2 = exam2

    def getExam2Grade(self):
        return self.__exam2

#finally, getting the average of the two exams....
    def getAverage(self):
        if self.__exam1 == None or self.__exam2 == None:
            print("Some exam grades not available.")
        else:
            return (self.__exam1 + self.__exam2)/2
    
    
