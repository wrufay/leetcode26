# First solved May 11, 2026

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # iterative, can also do recursive
        while root: # process each node at a time, starting with the root because pre-order traversal
            if root.left is not None: 
                # idea: store the original right subtree (child of root) in a temp pointer, then set the left subtree to be the right subtree.
                temp = root.right
                root.right = root.left
                # remove the original left subtree
                root.left = None


                # then iterate to the tail of the right subtree and that's where we will attach the temp
                tail = root.right
                while tail.right:
                    tail = tail.right
                tail.right = temp
                # dont forget to iterate when this is done
            root = root.right

        