import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s: str, n: int) -> int:
    len_s = len(s)
    count_a = s.count('a')
    reminder = n % len_s

    return n // len_s * count_a + s[:reminder].count('a')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    fptr.write(str(result) + '\n')
    fptr.close()

print(repeatedString("a", 1000000000000))