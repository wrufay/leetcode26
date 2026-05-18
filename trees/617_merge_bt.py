# First solved May 18, 2026

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # solve this recursively; base case first
        if root1 is None and root2 is None:
            # if both roots do not exist then, just return an empty tree
            return None
        
        if root1 and root2:
            # if both exist, make a new node with the sum both root values
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)

            # return the merged subtree so it can be attached
            return node
        
        if root1:
            return root1
        if root2:
            return root2
        
        