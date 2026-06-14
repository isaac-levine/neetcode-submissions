# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str: 

        res = ""
        q = deque()
        q.append(root)

        while q:
            for _ in range(len(q)):
                node = q.popleft() 
                res += str(node.val) if node else "#" # signifies null
                res += " "
                if node:
                    # do we need a separator as well? 
                    q.append(node.left)
                    q.append(node.right)

        return res 


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(" ")

        if not data or data[0] == "#": return None
        

        root = TreeNode(data[0])
        q = deque() 
        q.append(root)

        ptr = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft() 
                node.left = TreeNode(data[ptr]) if data[ptr] != "#" else None
                ptr += 1
                node.right = TreeNode(data[ptr]) if data[ptr] != "#" else None
                ptr += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root
