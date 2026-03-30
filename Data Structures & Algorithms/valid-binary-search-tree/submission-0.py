# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # For each substree we have an acceptable range
        # For the root, this acceptable range starts at [-inf, inf]
        def valid(node: Optional[TreeNode], minVal: int, maxVal: int) -> bool:
            if not node:
                return True
            elif not (minVal < node.val < maxVal): # ensure that this node is in between the two vals
                return False
            else:
                return valid(node.left, minVal, node.val) and valid(node.right, node.val, maxVal)

        return valid(root, float("-inf"), float("inf"))