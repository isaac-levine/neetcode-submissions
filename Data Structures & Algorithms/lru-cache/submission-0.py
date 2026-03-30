# Node representing a key,value pair in the cache
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        # left --> least recently used, remove from here
        self.left = Node(0, 0)

        # right --> most recently used, add to here 
        self.right = Node(0, 0)

        self.right.prev = self.left
        self.left.next = self.right

        self.capacity = capacity

    # Add the node one space to the left of the rightmost node
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    # Remove this node, connecting its prev and next nodes together
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Return the value corresponding to the key if the key exists, otherwise return -1.
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
        
    # Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
    # If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value) # update the value
        self.insert(self.cache[key])

        # check capacity
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        

