# First solved May 5, 2026

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # almost same thing as max depth but with the edge case of when we are at a leaf node, don't include that in the minumum calculation
        if root is None:
            return 0
            
        if root.left is None:
            return 1 + self.minDepth(root.right) # don't forget to add one, count the current node, we just don't count this depth as the minumum since it's a node with only one child
        if root.right is None:
            return 1 + self.minDepth(root.left)

        # otherwise, take the minimum of each subtree recursed on
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        