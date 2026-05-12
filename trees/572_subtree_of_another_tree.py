# First solved May 11, 2026

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None: # base case; can't have a subroot of nothing
            return False

        if self.sameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    # helper function, check if two trees are the same tree
    def sameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        # base case - both are null, same tree
        if root1 == None and root2 == None:
            return True
        
        # if one root is none and the other isn't then not the same
        if root1 == None or root2 == None:
            return False

        # compare the value of the root, if it's the same, recurse, otherwise immediately false
        if root1.val == root2.val:
            return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)
        else:
            return False

        
        

        
        