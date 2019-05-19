"""
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

For example, two is written as II in Roman numeral, just two one's added together. 
Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, 
which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, 
the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is 
before the five we subtract it making four. The same principle applies to the number nine, 
which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # temp is used to store and compare (less/greater) each number with the previous one
        temp = None
        result = 0
        for roman_num in s:
            int_num = roman_to_int_dict.get(roman_num)
            result += int_num
            if temp and int_num > temp:
                result -= 2*temp
            temp = int_num

        return result


s = Solution()
print(s.romanToInt('DXIV'))
