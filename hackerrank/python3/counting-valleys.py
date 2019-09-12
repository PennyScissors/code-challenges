#!/bin/python3

"""
Problem: Counting Valleys
Complete the countingValleys function in the editor below. 
It must return an integer that denotes the number of valleys Gary traversed.
"""

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n: int, s: str) -> int:
    valleys = 0
    level = 0
    flag = False

    for step in s:
        level += 1 if step == 'U' else -1
        
        if level < 0:
            flag = True
               
        if flag and level >= 0:
            flag = False
            valleys += 1

    return valleys
            
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     n = int(input())
#     s = input()
#     result = countingValleys(n, s)
#     fptr.write(str(result) + '\n')
#     fptr.close()

print(countingValleys(8, "UDDDUDUUDUDUDUDDUDUU")) # Correct answer is 5
