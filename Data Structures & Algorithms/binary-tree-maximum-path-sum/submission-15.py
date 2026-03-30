# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0 

        # maximum path sum can go through any root node
        res = root.val # entire tree can have negative vals, so initializing with root.val instead of 0

        # returns the maxHeight of the tree starting at root. 
        # updates res if the height pivoting at root is greater than res.
        def dfs(root):
            nonlocal res 
            if not root:
                return 0 

            leftMax, rightMax = dfs(root.left), dfs(root.right) 
            leftMax, rightMax = max(0, leftMax), max(0, rightMax) 

            res = max(res, root.val + leftMax + rightMax) 
            return root.val + max(leftMax, rightMax) 

        dfs(root)
        return res 
