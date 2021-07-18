#!/bin/python3

"""
Problem: Two Strings
Complete the function twoStrings in the editor below. 
It should return a string, either YES or NO based on whether the strings share a common substring.
"""

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1: str, s2: str) -> str:
    for c in s1:
        if c in s2:
            return "YES"
    return "NO"

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     q = int(input())
#     for q_itr in range(q):
#         s1 = input()
#         s2 = input()
#         result = twoStrings(s1, s2)
#         fptr.write(result + '\n')
#     fptr.close()

print(twoStrings("hello", "world")) # Correct answer is YES