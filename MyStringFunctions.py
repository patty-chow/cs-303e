# File: MyStringFunctions.py
# Student: Patty Chow
# UT EID: mpc2468
# Course Name: CS303E
# 
# Date Created: 03/30/2021
# Date Last Modified: 04/02/2021
# Description of Program: This program runs different functions for you depending on the strings or characters that you input.

"""
The only string functions/methods you can use in this assignment are:

    1. ord, chr
    2. indexing and slicing
    3. append (i.e., ``+'')
    4. len, in, not in
    5. equality comparison (== or !=))
"""

def myAppend( str_input, ch ):
    # Return a new string that is like str but with 
    # character ch added at the end
    return str_input + ch

def myCount( str, ch ):
    counter=0
    chCounter=0
    while(counter<len(str)):
        if(str[counter]==ch):
            chCounter= chCounter+1
        counter=counter+1
    return chCounter    


def myExtend( str1, str2 ):
    # Return a new string that contains the elements of
    # str1 followed by the elements of str2, in the same
    # order they appear in str2.
    return str1 + str2


def myMin( str ):
    counter=0
    if(len(str)==0):
        print ("Empty string: no min value")
        return None
    else:
        firstChar= str[0]
        while(counter<len(str)):
            if(ord(str[counter])<ord(firstChar)):
                firstChar= str[counter]
                counter= counter+1
            else:
                counter += 1
        return firstChar

        
def myInsert( str, i, ch ):
    # Return a new string like str except that ch has been
    # inserted at the ith position.  I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of str and return None.
    if(i>len(str)):
        print("Invalid index")
        return None
    elif(i==0):
        return ch+str
    else:
        return str[0:i]+ch+str[i:len(str)]



def myPop( str, i ):
    # Return two results: 
    # 1. a new string that is like str but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(str), and return str unchanged and None
    if(i>=len(str)):
        print("Invalid index")
        print("('"+str+"', None)")
    else:
        print("('"+str[0:i]+str[i+1:len(str)]+"', '"+str[i]+"')")



def myFind( str_input, ch ):
    # Return the index of the first (leftmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.
    indexNumber=-1
    count=0
    while(count<len(str_input)):
        if(str_input[count]==ch):
            indexNumber= count
            return indexNumber
        else:
            count += 1
    return indexNumber

        

def myRFind( str_input, ch ):
    # Return the index of the last (rightmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.
    indexNumber=-1
    count=len(str_input)-1
    while(count>-1):
        if(str_input[count]==ch):
            indexNumber= count
            return indexNumber
        else:
            count -= 1
    return indexNumber


def myRemove( str_input, ch ):
    # Return a new string with the first occurrence of ch 
    # removed.  If there is none, return str.
    indexNumber=-1
    count=0
    while(count<len(str_input)):
        if(str_input[count]==ch):
            indexNumber= count
            return str_input[0:indexNumber]+str_input[indexNumber+1:len(str_input)]
        else:
            count += 1
    return str_input

        

def myRemoveAll( str_input, ch ):
    # Return a new string with all occurrences of ch.
    # removed.  If there are none, return str.
    newString=""
    count=0
    while(count<len(str_input)):
        if(str_input[count]!=ch):
            newString= newString+str_input[count]
            count += 1
        else:
            count += 1
    return newString


def myReverse( str_input ):
    # Return a new string like str but with the characters
    # in the reverse order.
    newString=""
    count=len(str_input)-1
    while(count>-1):
        newString= newString+str_input[count]
        count -= 1
    return newString



"""
>>> from MyStringFunctions import *
>>> s1 = "abcd" 
>>> s2 = "efgh"
>>> myAppend( s1, "e" )
'abcde'
>>> myCount( s1, "e")
0
>>> myCount( s1, "a")
1
>>> myCount( "abcabc", "a")
2
>>> myExtend( s1, s2 )
'abcdefgh'
>>> myMin( "" )
Empty string: no min value    # Note the None doesn't print
>>> myMin( "zqralm" )
'a'
>>> myMin( "Hello World!" )
' '
>>> myInsert( "abc", 0, "d")
'dabc'
>>> myInsert( "abc", 2, "d")
'abdc'
>>> myInsert( "abc", 4, "d")     
Invalid index                 # Note the None doesn't print
>>> myPop( "abcd", 1 )
('acd', 'b')
>>> myPop( "abcd", 0 )
('bcd', 'a')
>>> myPop( "abcd", 5)
Invalid index
('abcd', None)
>>> myFind( "abcdabcd", "a")
0
>>> myFind( "abcdabcd", "c")
2
>>> myFind( "abcdabcd", "f")
-1
>>> myRFind("abcdabcd", "d")
7
>>> myRFind("abcdabcd", "e")
-1
>>> myRemove( "abcdabcd", "a")
'bcdabcd'
>>> myRemove( "abcdabcd", "x")
'abcdabcd'
>>> myRemove( "abcdabcd", "d")
'abcabcd'
>>> myRemoveAll("abcabcabca", "a")
'bcbcbc'
>>> myReverse( "abcd" )
'dcba'
>>> myReverse( "" )
''

"""
