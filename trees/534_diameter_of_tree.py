# First solved May 15, 2026

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # base case
        if root is None:
            return 0

        self.max_diameter = 0
        self.height(root) # just call the helper, it modifies this value
        
        return self.max_diameter
        
        # understand: the diameter of a binary tree at any node is the height of the right subtree plus the height of the left subtree at that node. then we just want to find the max diameter as we traverse each node.
        
    # recursive helper function that calculates the height (max depth) of a tree, and updates max_depth as a side effect
    def height(self, root: Optional[TreeNode]) -> int:
        # base case
        if root is None:
            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)

        self.max_diameter = max(left + right, self.max_diameter)

        return 1 + max(left, right)
        

        
        
        

        
        