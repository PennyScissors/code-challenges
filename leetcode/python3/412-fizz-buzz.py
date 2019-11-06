"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of 
five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return_list = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                return_list.append("FizzBuzz")
            elif i % 3 == 0:
                return_list.append("Fizz")
            elif i % 5 == 0:
                return_list.append("Buzz")
            else:
                return_list.append(str(i))

        return return_list
 

print(Solution().fizzBuzz(10))
print(Solution().fizzBuzz(0))
