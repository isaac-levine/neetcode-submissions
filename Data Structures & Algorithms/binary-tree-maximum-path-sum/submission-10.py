# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = root.val

        def dfs(node):
            nonlocal res # or just make res a list so you can modify it in here
            if not node:
                return 0
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)
            res = max(res, node.val + leftMax + rightMax) # use this as the root 
            return node.val + max(leftMax, rightMax) # pick a side 

        dfs(root)

        return res
        