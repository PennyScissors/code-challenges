#!/bin/python3

"""
Problem: 2D Array DS
Complete the function hourglassSum in the editor below. 
It should return an integer, the maximum hourglass sum in the array.
"""

import math
import os
import random
import re
import sys

from typing import List

# Complete the hourglassSum function below.
def hourglassSum(arr: List[List[int]]) -> int:
    max_sum = None
    end = len(arr) - 2
    for row in range(0, end):
        for col in range(0, end):
            hourglass_sum = sum(arr[row][col:col + 3]) + \
                            arr[row + 1][col + 1] + \
                            sum(arr[row + 2][col:col + 3])
            if not max_sum and max_sum != 0:
                max_sum = hourglass_sum
            elif hourglass_sum > max_sum:
                max_sum = hourglass_sum
        
    return max_sum
    

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     arr = []
#     for _ in range(6):
#         arr.append(list(map(int, input().rstrip().split())))
#     result = hourglassSum(arr)
#     fptr.write(str(result) + '\n')
#     fptr.close()

test_arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]

print(hourglassSum(test_arr)) # Correct answer is 19
