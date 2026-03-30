"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    
        # first pass 
        cur = head 
        oldToNew = {None : None} 
        while cur: 
            oldToNew[cur] = Node(cur.val, None, None) 
            cur = cur.next


        # second pass (follow the pointers)
        cur = head
        while cur:
            oldToNew[cur].next = oldToNew[cur.next]
            oldToNew[cur].random = oldToNew[cur.random]
            cur = cur.next

        return oldToNew[head]
            

