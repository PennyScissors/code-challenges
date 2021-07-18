#!/bin/python3

import math
import os
import random
import re
import sys

from typing import List

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c: List[int]) -> int:
    steps = 0
    last_index = len(c) - 1
    i = 0

    while i < last_index:
        if i + 2 <= last_index and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        steps += 1
    
    return steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()

print(jumpingOnClouds([0,0,0,0,1,0,1,0]))