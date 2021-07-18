#!/bin/python3

"""
Problem: Hash Tables: Ransom Note
Complete the checkMagazine function in the editor below. 
It must print YES if the note can be formed using the magazine, or NO.
"""

import math
import os
import random
import re
import sys

from typing import List

# Complete the checkMagazine function below.
def checkMagazine(magazine: List[str], note: List[str]) -> bool:
    mag_word_count = {}

    for word in magazine:
        mag_word_count.setdefault(word, 0)
        mag_word_count[word] += 1
    
    for word in note:
        try:
            mag_word_count[word] -= 1
            if mag_word_count[word] < 0:
                print("No")
                return
        except KeyError:
            print("No")
    print("Yes")

# if __name__ == '__main__':
#     mn = input().split()
#     m = int(mn[0])
#     n = int(mn[1])
#     magazine = input().rstrip().split()
#     note = input().rstrip().split()
#     checkMagazine(magazine, note)

magazine = ["give", "me", "one", "grand", "today", "night"]
note = ["give", "one", "grand", "today"]
print(checkMagazine(magazine, note)) # Correct answer is True
