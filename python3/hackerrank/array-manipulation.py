#!/bin/python3

"""
Problem: Array Manipulation
https://www.hackerrank.com/challenges/crush/problem
"""

import math
import os
import random
import re
import sys

from typing import List

# Complete the arrayManipulation function below.
def arrayManipulation(n: int, queries: List[int]) -> int:
    l = [0] * (n + 1)
    max_num = 0
    max_temp = 0
    for query in queries:
        a, b, k = query
        l[a] += k
        if (b + 1 <= n):
            l[b + 1] -= k
    for num in l:
        max_temp += num
        if max_temp > max_num:
            max_num = max_temp

    return max_num

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     nm = input().split()
#     n = int(nm[0])
#     m = int(nm[1])
#     queries = []
#     for _ in range(m):
#         queries.append(list(map(int, input().rstrip().split())))
#     result = arrayManipulation(n, queries)
#     fptr.write(str(result) + '\n')
#     fptr.close()
 
n = 5
queries = [
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100]
]

n_2 = 10
queries_2 = [
    [1, 5, 3],
    [4, 8, 7],
    [6, 9, 1]
]

n_3 = 10
queries_3 = [
    [2, 6, 8],
    [3, 5, 7],
    [1, 8, 1],
    [5, 9, 15]
]

print(arrayManipulation(n, queries)) # Correct answer is 200
print(arrayManipulation(n_2, queries_2)) # Correct answer is 10
print(arrayManipulation(n_3, queries_3)) # Correct answer is 31
 