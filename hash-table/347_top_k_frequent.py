# First solved June 6, 2026

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first, use a hashmap to count the frequencies, with each number as a key and the frequency as the value
        nums_map = {}

        for num in nums:
            if num not in nums_map:
                nums_map[num] = 1
            else:
                nums_map[num] += 1
        
        # next we need to sort the map by its frequency - can sort normally and then take the last k elements

        # sorted function returns a list of the sorted keys of a dict by default, use a lambda function to make it sort by the value

        # [-k:] takes the last k elements

        return sorted(nums_map, key=lambda x: nums_map[x])[-k:]





        