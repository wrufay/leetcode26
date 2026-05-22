# First solved May 22, 2026

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        else: return self.isUnivalTreeAcc(root, root.val)

    def isUnivalTreeAcc(self, node, prev):
        # keep track of the previous value and compare
        if node is None:
            return True
        if node.val != prev:
            return False
        else:
            return self.isUnivalTreeAcc(node.left, node.val) and self.isUnivalTreeAcc(node.right, node.val)

        