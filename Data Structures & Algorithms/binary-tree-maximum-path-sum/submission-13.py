# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        

        # need to know two things for every root. 
        # 1. RETURN the value my maximum path sum in one direction (or 0)
        # 2. STORE the maximum path sum going "through" me. i.e. using me as the one and only root. this is what we update res with  

        res = root.val
        
        def dfs(root):
            nonlocal res
            if not root:
                return 0 

            leftMax, rightMax = max(0, dfs(root.left)), max(0, dfs(root.right))
            res = max(res, root.val + leftMax + rightMax) # store the maximum path going through me / using me as the root 

            return root.val + max(leftMax, rightMax)  

        dfs(root)
        return res 
