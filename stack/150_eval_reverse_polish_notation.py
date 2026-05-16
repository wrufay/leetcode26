# First solved May 15, 2026
# Quest: DSA - Stack Q2)

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                # if symbol, remove two numbers and perfom that operation
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                result = 0
                if token == '+':
                    result = num1 + num2
                if token == '*':
                    result = num1 * num2
                if token == '-':
                    result = num2 - num1
                if token == '/':
                    result = int(num2 / num1) # don't forget to truncate, and order matters
                stack.append(result) # push the result onto the stack
            else:
                # push the number onto the stack
                stack.append(int(token))
        
        return stack[0]
