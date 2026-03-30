# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if not a and not b:
                return True
            elif (a and not b) or (b and not a):
                return False
            else:
                return a.val == b.val and (sameTree(a.left, b.left) and sameTree(a.right, b.right))

        def dfs(node):
            if not node:
                return False    
            if sameTree(node, subRoot):
                return True
            else:
                return dfs(node.left) or dfs(node.right)    

        
        return dfs(root)
