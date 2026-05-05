# First solved May 5, 2026

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # idea: iterate and compare each value
        
        # base case
        if q is None and p is None:
            # got to the end of both, return true
            return True

        # 3 cases that mean they are not the same tree; if one is at the end, or if the values of their root node is not the same
        
        if q is None or p is None: return False

        if q.val != p.val: return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



        