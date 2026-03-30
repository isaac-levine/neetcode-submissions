# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = float("-inf")

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            else:
                leftMax = max(dfs(node.left), 0)
                rightMax = max(dfs(node.right), 0)
                nodeMax = max(node.val, node.val + leftMax, node.val + rightMax, node.val + leftMax + rightMax)
                res = max(res, nodeMax)
                return node.val + max(leftMax, rightMax)

        dfs(root)

        return res
        