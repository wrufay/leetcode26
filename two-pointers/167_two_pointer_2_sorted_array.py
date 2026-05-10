# First solved May 10, 2026

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        result = []

        while l != r:
            if numbers[l] + numbers[r] == target:
                result.append(l + 1)
                result.append(r + 1) 
                return result # don't forget to return immediately
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return result

        