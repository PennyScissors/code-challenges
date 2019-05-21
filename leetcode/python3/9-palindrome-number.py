class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            num_list = list(str(x))

            # Check if num_list is equal to a copy in reverse order
            return num_list == num_list[::-1]


print(Solution().isPalindrome(12321))
