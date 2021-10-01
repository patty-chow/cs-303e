# File: ComparingLinearBinarySearch.py
# Student: Patty Chow
# UT EID: mpc2468
# Course Name: CS303E
# 
# Date Created: 04/16/2021
# Date Last Modified: 04/16/2021
# Description of Program: This program compares the performance of linear and binary search. It's divided into two sections where, at the end, the average number of probes are compared.

def linearSearch( lst, key ):
    """ Search for key in unsorted list lst.  Note that
        the index + 1 is also the number of probes. """
    for i in range( len(lst) ):
        if key == lst[i]:
            return i
    return -l

 

def binarySearch( lst, key ):
    """ Search for key in sorted list lst. Return
        a pair containing the index (or -low - 1)
        and a count of number of probes. """
    count = 0
    low = 0
    high = len(lst) - 1
    while (high >= low):
        count += 1
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return (mid, count)
        else:
            low = mid + 1
    # Search failed
    return (-low - 1, count)

 

import math
import random
def main():
    val = [i for i in range(1000)]
    random.shuffle(val)
 
    count = 0
    average = 0
    i = 0
 
    while i > 10 or i < 10:
        key = random.randint(0,999)
        count = linearSearch(val, key) + 1
        average += count
        i += 1
 
    print("Linear search:" "\n"+
          "  Tests:", str(10), "    Average probes:", str(average/10))
 
    count = 0
    average = 0
    i = 0
   
    while i > 100 or i < 100:
        key = random.randint(0,999)
        count = linearSearch(val, key) + 1
        average += count
        i += 1
 
    print("  Tests:", str(100), "   Average probes:", str(average/100))
 
    count = 0
    average = 0
    i = 0
 
    while i > 1000 or i < 1000:
        key = random.randint(0,999)
        count = linearSearch(val, key) + 1
        average += count
        i += 1
 
    print("  Tests:", str(1000), "  Average probes:", str(average/1000))
 
    count = 0
    average = 0
    i = 0
 
    while i > 10000 or i < 10000:
        key = random.randint(0,999)
        count = linearSearch(val, key) + 1
        average += count
        i += 1
 
    print("  Tests:", str(10000), " Average probes:", str(average/10000))
 
    count = 0
    average = 0
    i = 0
 
    while i > 100000 or i < 100000:
        key = random.randint(0,999)
        count = linearSearch(val, key) + 1
        average += count
        i += 1
 
    print("  Tests:", str(100000), "Average probes:", str(average/100000))
 
#Binary Search
    count = 0
    average = 0
    i = 0
   
    while i > 1000 or i < 1000:
        key = random.randint(0,999)
        count = binarySearch(val, key)[1]
        average += count
        i += 1
 
    differsLog2 = abs(average/1000 - math.log(1000,2))
 
    print("Binary search: \n"
          "  Average number of probes:", str(average/1000), "\n"
          "  Differs from log2(1000) by:", str(differsLog2))
 
 
main()