# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        res = ""

        def dfs(node):
            nonlocal res
            if not node:
                res += ("N,")
                return
            res += (str(node.val) + ",")
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:

        nums = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            if nums[i] == "N":
                i += 1
                return None
            node = TreeNode(int(nums[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

