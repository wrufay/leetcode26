# First solved May 13, 2026

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window method, use a set to store seen characters for O(1) lookup
        seen = set() # stores what's currently in the window
        l = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in seen:
                # slide the window by increasing l and removing that char from the set
                # idea: while the right character is in the window, move l forward until it's not.
                seen.remove(s[l]) # change what's in the window
                l += 1 # shift
            
            seen.add(s[r]) # add the current char into the window, r also increments in the loop
            

            # update max length each iteration for returning
            if r - l + 1 > max_len:
                max_len = r - l + 1

        return max_len




        
        




        
        