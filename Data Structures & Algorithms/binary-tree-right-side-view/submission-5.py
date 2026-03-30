# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # perform a level order traversal but only add right-most nodes to res 
        res = [] 
        pq = deque() 
        pq.append(root)

        while pq:

            # process everything on this level
            level = []
            for i in range(len(pq)):
                node = pq.popleft() 
                if not node:
                    continue
                level.append(node.val)
                if node.left:
                    pq.append(node.left)
                if node.right:
                    pq.append(node.right) 
            
            # add right-most node of this level to the res
            if level:
                res.append(level.pop())

        return res 
