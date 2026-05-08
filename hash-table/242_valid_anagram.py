# First solved May 7, 2026

from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # add everything to the set, where key = letter, value = occurences of that letter
        if len(s) != len(t): return False

        letters_s = {}
        letters_t = {}

        for letter in s: letters_s[letter] = letters_s.get(letter, 0) + 1
        for letter in t: letters_t[letter] = letters_t.get(letter, 0) + 1


        for letter in t:
            if letters_t[letter] != letters_s.get(letter, 0):
                return False
        
        return True



        
        