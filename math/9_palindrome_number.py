# First solved May 8, 2026

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # two pointers
        my_str = str(x)
        my_len = len(my_str)
        for i in range(my_len):
            if my_str[i] != my_str[my_len - i - 1]:
                return False

        return True
        