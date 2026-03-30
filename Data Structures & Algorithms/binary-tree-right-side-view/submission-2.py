# You are given the root of a binary tree.
# Return only the values of the nodes that are visible from the
# right side of the tree, ordered from top to bottom.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = [] 
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            last = None
            for i in range(qLen):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right) 
                    last = node 
            if last:
                res.append(last.val)
        return res
