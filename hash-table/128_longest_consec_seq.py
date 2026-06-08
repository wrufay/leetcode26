# First solved June 7, 2026

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use a set to check if each number is the start of a consecutive sequence, can initialize it with this syntax easily
        num_set = set(nums)

        max_len = 0
        
        # loop, see if each num is the start of a consecutive sequence - tuff trick
        for num in num_set: # make sure this is num_set not nums we don't want to do duplicates
            if num - 1 not in num_set:
                # start of a sequence, continue the length as we continue
                count = 1
                while count + num in num_set:
                    count += 1
                max_len = max(count, max_len)

        return max_len
        

            
        