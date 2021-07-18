#!/bin/python3
"""
Problem: Left Rotation
https://www.hackerrank.com/challenges/array-left-rotation/problem
"""

import math
import os
import random
import re
import sys

def rotate_left(a, d):
    d = d % len(a)
    return a[d:] + a[:d]

if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    a = rotate_left(a, d)
    print(*a)
