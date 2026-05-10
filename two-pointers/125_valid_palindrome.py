# First solved May 10, 2026

from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower() # convert to lowercase

        l = 0
        r = len(s) - 1

        while l < r:
            if not string[l].isalnum():
                l += 1
            elif not string[r].isalnum():
                r -= 1
            elif string[l] != string[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

        