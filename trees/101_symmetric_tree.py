# First solved May 16, 2026

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.compare(root.left, root.right)
    
    # helper function that checks if two trees are symmetric to each other
    def compare(self, left, right):
        if not left and not right:
            return True
        # cases that would be false
        if left and not right:
            return False
        if right and not left:
            return False
        
        if left and right and left.val != right.val: # note we use != not is not for value comparison!
            return False
        
        # difference from comparing symmetry with same is how we recurse
        return self.compare(left.left, right.right) and self.compare(right.left, left.right)

        