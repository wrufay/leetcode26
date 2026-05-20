# First solved May 18, 2026

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # use accumulative recursion 
        return self.hasPathSumAcc(root, targetSum, 0)

    # make a helper function that keeps track of the sum
    def hasPathSumAcc(self, node, targetSum, curSum):
        if node is None: # if no tree then automatically false
            return False

        # base case, check if we are at a leaf node
        if not node.left and not node.right:
            # just check this path
            return curSum + node.val == targetSum
        
        # otherwise if not leaf node, recurse while adding current node's value to the current sum
        return self.hasPathSumAcc(node.left, targetSum, curSum + node.val) or self.hasPathSumAcc(node.right, targetSum, curSum + node.val)



        

        


        