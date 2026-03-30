class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.right.prev = self.left
        self.left.next = self.right
        self.cache = {} # key -> ListNode

    # return the value corresponding to key, otherwise -1 if it does not exist
    # must be O(1) time
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insertAtRight(node)
            return node.val
        else:
            return -1 

    # update the value of key if the key exists. otherwise add the key-value pair to the cache. if the introduction of the new pair causes the cache to exceed its capacity, remove the LRU key
    # must be O(1) time
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insertAtRight(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
        
        
    # remove this node and connect its prev to its next
    def remove(self, node: ListNode) -> None:
        prev, nxt = node.prev, node.next 
        prev.next = nxt
        nxt.prev = prev 

    # insert one space to the left of the rightmost node
    def insertAtRight(self, node: ListNode) -> None: 
        prev, nxt = self.right.prev, self.right
        node.next = nxt
        node.prev = prev
        prev.next = node
        nxt.prev = node 
        
