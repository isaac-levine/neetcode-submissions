# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pq = deque() 
        pq.append(root)
        res = []

        if not root:
            return res 

        while pq:
            # for the current size of the pq at this snapshot in time
            level = []
            for i in range(len(pq)):
                node = pq.popleft() 
                if not node:
                    continue
                pq.append(node.left)# appends to the right
                pq.append(node.right) # ""
                level.append(node.val) # "" 
            if level:
                res.append(level)
        return res 
