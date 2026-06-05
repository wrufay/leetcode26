# First solved June 5, 2026

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap - use the sorted version of each word as a key.
        words = {}
        result = []

        for word in strs:
            # note, the sorted function turns the string into an array so we need to join them after
            sorted_word = ''.join(sorted(word))

            if sorted_word in words:
                words[sorted_word].append(word)
            
            else:
                # if the key is not there, then add it
                # ok so what is the value
                # the value is going to be an array, initially empty and whenever we get to a word that is an anagram of this word, add it to the array
                words[sorted_word] = [word]
            # then for the final result we just put the valu eo fthe key in easch uhh ye ykwim c
            #crine i cant explain for buns
            # chopped logic
            # result.append(words[sorted_word])
            # this is wrong oops

        return list(words.values())
        

        