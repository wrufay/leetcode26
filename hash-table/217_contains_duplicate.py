# First solved May 7, 2026

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create an empty hash set
        all_nums = set()
        # Loop through the `nums` array
        for num in nums:
            # At each element, check if that number already exists in the hashmap.
            if num in all_nums:
                # If it does - short circuit, return `true`
                return True
                # Otherwise, add that element to the hashmap and proceed looping through the array.
            else:
                all_nums.add(num)
        
        # Once we've looped through the entire array and no duplicate is found, return `false`
        return False

        