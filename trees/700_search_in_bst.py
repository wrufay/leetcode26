# First solved May 5, 2026

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None # base case

        if root.val == val:
            return root
        elif val < root.val:
            # search left subtree
            return self.searchBST(root.left, val)
        else:
            # search right subtree
            return self.searchBST(root.right, val)