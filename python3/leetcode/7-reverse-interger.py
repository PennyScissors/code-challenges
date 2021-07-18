"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
    Input: 123
    Output: 321
Example 2:
    Input: -123
    Output: -321

Example 3:
    Input: 120
    Output: 21

Note:
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    def reverse(self, x: int) -> int:
        # If negative, remove the sign so the number can be reversed more easily
        is_neg = x < 0
        if is_neg:
            x *= -1

        # Reverse the number
        x_rev = 0
        while int(x) >= 1:
            last_digit = int(x) % 10
            x_rev = x_rev * 10 + last_digit
            x /= 10

        # Check if the result overflows the 32 bit signed integer's range
        if x_rev < (-1 << 31) or x_rev > ((1 << 31) - 1):
            return 0

        return x_rev * -1 if is_neg else x_rev


solution = Solution()
print(solution.reverse(-120)) # correct: -21
print(solution.reverse(900000)) # correct: 9
print(solution.reverse(1534236469)) # overflows, should return 0
