# First solved May 7, 2026

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_map = {}
        for num in nums:
            if num in nums_map:
                return True
            else:
                nums_map[num] = True
                # uhh could also use a set to be cleaner since we don't need key value pairs for this question.
        
        return False


        