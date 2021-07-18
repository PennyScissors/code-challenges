#!/bin/python3

"""
Problem: Arrays: Left Rotation
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
"""

import math
import os
import random
import re
import sys

from typing import List

# Complete the rotLeft function below.
def rotLeft(a: List[int], d: int) -> List[int]:
    d = d % len(a)
    a += a[:d]
    del a[:d]

    return a

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     nd = input().split()
#     n = int(nd[0])
#     d = int(nd[1])
#     a = list(map(int, input().rstrip().split()))
#     result = rotLeft(a, d)
#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')
#     fptr.close()

print(rotLeft([1,2,3,4,5], 13)) # Correct answer is [4,5,1,2,3]
