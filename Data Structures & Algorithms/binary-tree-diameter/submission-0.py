# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        
        # this dfs is answering the question: 
        # make the maxDiameter the max of itself and the sum of left and right
        # and return up to my caller, my maxHeight
        def dfs(node):
            nonlocal maxDiameter 

            if not node:
                return 0 
            
            left = dfs(node.left)
            right = dfs(node.right)
            maxDiameter = max(maxDiameter, left + right) 
            return 1 + max(left, right)
        
        dfs(root)
        return maxDiameter
