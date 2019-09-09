#!/bin/python3

import math
import os
import random
import re
import sys

from typing import List

# Complete the sockMerchant function below.
def sockMerchant(n: int, ar: List[int]) -> int:
    candidates = []
    pairs = 0
    for sock in ar:
        if sock in candidates:
            candidates.remove(sock)
            pairs += 1
        else:
            candidates.append(sock)

    return pairs

def sockMerchant_2(n: int, ar: List[int]) -> int:
    pairs = 0
    while ar:
        color = ar.pop()
        try:
            ar.remove(color)
            pairs += 1
        except ValueError:
            pass
        
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()

print(sockMerchant(6, [0,1,2,2,6,1,1]))