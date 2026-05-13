# First solved May 13, 2026

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # use the niche method from add two numbers the og lc crine
        result = ""

        i = len(a) - 1
        j = len(b) - 1
        carry = 0

        while i >= 0 and j >= 0:
            cur_sum = int(a[i]) + int(b[j]) + carry
            carry = cur_sum // 2
            result += str(cur_sum % 2)
            i -= 1
            j -= 1

        while i >= 0:
            cur_sum = int(a[i]) + carry
            carry = cur_sum // 2
            result += str(cur_sum % 2)
            i -= 1

        while j >= 0:
            cur_sum = int(b[j]) + carry
            carry = cur_sum // 2
            result += str(cur_sum % 2)
            j -= 1

        if carry: result += '1'
        

        # reverse at the end
        return result[::-1]
        