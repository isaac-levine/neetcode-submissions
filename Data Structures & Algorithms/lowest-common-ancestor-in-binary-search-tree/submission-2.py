# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # LCA -- lowest root in the tree s.t. both p and q are decendants  
        # i.e. left contains p and right contains q. or left contains q and right contains p 
        # all root.vals are unique 

        # dont want to just iterate through asking each side if it contains both 
        
        # we know the value must be <= one and >= the other.  

        # Q: is this the thing where we want to pass some sort of maximum and minimum to define a range? 
        
        if not root:
            return None
        elif (p.val <= root.val <= q.val) or (q.val <= root.val <= p.val):
            return root
        elif root.val >= p.val and root.val >= q.val:
            # greater, must be in the left subtree 
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val <= p.val and root.val <= q.val:
            # less, must be in the right subtree
            return self.lowestCommonAncestor(root.right, p, q)
                
