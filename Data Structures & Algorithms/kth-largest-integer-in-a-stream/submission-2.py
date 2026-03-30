class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) # O(n log n)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) 


    # 1. Add val to the stream
    # 2. Return kth largest integer in the stream
    # O(k) 
    def add(self, val: int) -> int:
        # loop through the nums
        # add if necessary
        # truncate if len > k
        if self.minHeap and val <= self.minHeap[0]:
            return self.minHeap[0]
        else:
            heapq.heappush(self.minHeap, val)
            # only pop if len > k
            if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap) 

        return self.minHeap[0]
