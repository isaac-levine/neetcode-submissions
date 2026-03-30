# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # return the kth smallest (1-indexed) value in the tree
        
        # could do O(N) traversal of tree, to build list of values
        # then just heapify O(N log N) 
        # 
        # values = []
        count = k
        res = root.val

        # In order traversal of the tree 
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

