
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
    
        # preorder : root -> left -> right
        # inorder : left -> root -> right


        # always know that preorder[0] is the root if this subtree. 

        # you know that inorder.index(preorder[0+1]) is the root val of the right subtree.

        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # tells you a lot, the index is equal to the size of the left subtree. so you can use it for slicing both the preorder and the inorder arrays. 
        # in inorder, the right subtree starts with index mid + 1
        # in preorder, the left subtree is the first mid numbers after the 0th. 

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

