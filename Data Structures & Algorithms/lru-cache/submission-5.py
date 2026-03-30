class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> ListNode

        self.left = ListNode(0, 0) # left.next is the least recently used
        self.right = ListNode(0, 0) # right.prev is the most recently used

        # need to remember to connect right to left, or else we don't even have a linked list 
        self.left.next = self.right
        self.right.prev = self.left


    # Return the value corresponding to the key if the key exists, otherwise return -1.
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insertAtRight(node) 
            return node.val
        else:
            return -1 


    # Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = ListNode(key, value) 
        self.insertAtRight(node) 
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)
        

    # BELOW METHODS ARE STRICTLY FOR LINKED LIST MANIPULATION  
    def insertAtRight(self, node: ListNode):
        prev, nxt = self.right.prev, self.right

        prev.next = node
        node.prev = prev 

        node.next = nxt
        nxt.prev = node 


    def remove(self, node: ListNode):
        prev, nxt = node.prev, node.next

        prev.next = nxt
        nxt.prev = prev 
