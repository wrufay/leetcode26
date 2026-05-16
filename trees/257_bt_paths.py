# First solved May 16, 2026

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # returning list of strings in the given format. *** use helper for accumulative recursion
        result = []
        self.path(root, "", result)
        return result

        
    # idea: helper function that takes in the result as a parameter and the current path, if end of tree then take the current path and add that to the result list. otherwise, recurse on left and right subtrees.

    def path(self, node: Optional[TreeNode], current_path: Optional[str], result: Optional[List[str]]) -> None:
        # base case
        if node is None:
            return

        # add current node value to the current path
        current_path += str(node.val)

        if not node.left and not node.right: # we are at a leaf node, stop
            # add current path to array
            result.append(current_path)
        else:
            # continue searching for next
            current_path += "->"
            
            # dont return anything, just recurse now by calling
            self.path(node.left, current_path, result)
            self.path(node.right, current_path, result)
        