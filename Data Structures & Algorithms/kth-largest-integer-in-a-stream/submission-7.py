class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # initialize a minHeap with the values from the kth largest to the 1st largest 
        # so it will have k values total. 
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap) # this is O(n) but naive analysis gives O(n log n)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) # make sure it only has k values total 
        

    # just add it to the heap and then pop off anything smaller than the kth largest. 
    # you know the top of the minHeap is the kth largest at all times so you can just return that when you're done.
    # O(log k)
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # O(log k) operation
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # O(log k) operation at most 1 time? 
        return self.minHeap[0]