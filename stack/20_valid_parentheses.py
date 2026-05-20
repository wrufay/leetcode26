# First solved May 20, 2026

class Solution:
    def isValid(self, s: str) -> bool:
        # stack
        stack = []

        # iterate through each character in the string, check for each type of bracket
        for char in s:
            # if it's an open bracket
            if char == '[' or char == '{' or char == '(':
                # push onto the strack
                stack.append(char)
            else:
                # otherwise if we have a closing bracket, check if it matches with the top element on the stack

                # rememember the case where the stack is empty and we try to put a closing bracket, automatically false.
                # make sure not to mess up the check between brackets
                if not stack or (char == ')' and stack[-1] != '(') or (char == ']' and stack[-1] != '[') or (char == '}' and stack[-1] != '{'):
                    return False
                else: # if does match, pop it off
                    stack.pop()


        return stack == [] # want to check if the stack is empty which means all the brackets have been closed
        