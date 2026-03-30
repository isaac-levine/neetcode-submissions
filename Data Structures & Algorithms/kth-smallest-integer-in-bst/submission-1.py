# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # use recursion to traverse all the way down to left 
        # then once you hit it, decrement k
        # if i ever get k == 1 that means i am the answer 
        

        count = k 
        res = root.val


        def dfs(node):
            nonlocal count, res
            
            if not node:
                return

            dfs(node.left)
            count -= 1

            if count == 0:
                res = node.val 
                return

            dfs(node.right) 
                
        dfs(root)
        return res 
