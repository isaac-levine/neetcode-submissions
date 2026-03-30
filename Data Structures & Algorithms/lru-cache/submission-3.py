# doubly linked list node  
class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> ListNode
        self.left = ListNode(0, 0) # left.next represents least recently used, right.prev represents most recently used
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # Return the value corresponding to the key if the key exists, otherwise return -1.
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insertAtRight(node)
            return self.cache[key].val # shouldnt matter but node.val
        else:
            return -1  
    
    # Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove the node
            self.remove(self.cache[key])
        # create a new node
        node = ListNode(key, value)
        # insert a new node at right
        self.insertAtRight(node)
        # reassign cache value 
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)

    # insert this node at right.prev, making it the most recently used node 
    def insertAtRight(self, node: ListNode) -> None:
        prev, nxt = self.right.prev, self.right

        node.next = nxt 
        nxt.prev = node

        prev.next = node
        node.prev = prev


    # connect its prev to its next, effectively removing the node
    def remove(self, node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
