# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    
        # preorder - root -> left subtree -> right subtree
        # inorder - left subtree -> root -> right subtree

        # first value in preorder traversal is always the root, and then determining what the rest is after that requires the inorder 

        # find that root (from above) in the inorder list. you know everything to the left of that root is in the left subtree, and everything to the right of it is in the right subtree. 

        # when you only have 1 node, (list of size 1) you know to return because you are the node. (recursive base case) 

        if not preorder or not inorder:
            return None 
       
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) 
        
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
         
        return root

