# First solved May 14, 2026
# Quest: DSA - Array II Q3)

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # store all number in nums in the set then loop through 1 to n and check if its in the set or not
        nums_set = set()
        result = []
        for num in nums:
            nums_set.add(num)
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                # can we reduce space by changing in place idk
                result.append(i)

        return result

        