# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            # determine the height and the balance (t/f) in a single traversal
            if not node:
                return [0, True]
            else:
                leftHeight, leftBalanced = dfs(node.left)
                rightHeight, rightBalanced = dfs(node.right)
                rootBalanced = abs(leftHeight - rightHeight) <= 1 
                return [1 + max(leftHeight, rightHeight), rootBalanced and leftBalanced and rightBalanced]  

        _, balanced = dfs(root) 
        return balanced
