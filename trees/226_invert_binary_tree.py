# First solved May 5, 2026

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if(root == None):
            return None
        else: 
            # invert left and right subtrees recursively, store them in a variable
            left = self.invertTree(root.left) 
            right = self.invertTree(root.right)

            # set the left and right subtrees to be the fully inverted trees
            root.left = right
            root.right = left

            # need to return the root of the inverted tree back so it can be used in subsequent recursive calls
            return root
        
        