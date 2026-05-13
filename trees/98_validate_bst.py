# First solved May 12, 2026

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def validate(self, node, min_val, max_val) -> bool:
        if node is None:
            return True
        
        # compare the current node's value to the min and max
        if node.val <= min_val or node.val >= max_val:
            return False
        
        
        return self.validate(node.left, min_val, node.val) and self.validate(node.right, node.val, max_val)

        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf'))
        