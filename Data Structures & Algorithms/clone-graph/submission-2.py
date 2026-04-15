"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldToNew = {} 

        def clone(old):
            if not old:
                return None
            if old in oldToNew:
                return oldToNew[old]

            new = Node(old.val)
            oldToNew[old] = new # add new into the hashmap now so that future recursions for neighbors can use it in the cache

            for nei in old.neighbors:
                new.neighbors.append(clone(nei))

            return new
        

        return clone(node)
        