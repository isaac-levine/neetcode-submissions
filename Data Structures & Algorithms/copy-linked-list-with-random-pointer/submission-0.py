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
        
        # first pass: make all the nodes with values and add to hashmap of old -> new
        oldToNew = {None : None} # empty entry  
        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val, None, None)
            curr = curr.next 


        # second pass: add all the "next" and "random" links
        curr = head
        while curr:
            oldToNew[curr].next = oldToNew[curr.next]
            oldToNew[curr].random = oldToNew[curr.random]
            curr = curr.next

        return oldToNew[head]
        