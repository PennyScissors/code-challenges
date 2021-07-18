from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [a for x in zip(nums[:n], nums[n:]) for a in x]

print(Solution().shuffle([1,2,3,4,4,3,2,1], 4))
