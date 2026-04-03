# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        res = [] 

        def dfs(node: Optional[TreeNode]):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left) # fine as long as we do it in the exact same root -> left -> right order as above.
            dfs(node.right)
            
        dfs(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        self.i = 0

        def dfs():
            if self.i >= len(values) or values[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = dfs() # fine as long as we do it in the exact same root -> left -> right order as above.
            node.right = dfs()
            return node
        
        return dfs()

