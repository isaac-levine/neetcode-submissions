class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        # we only need a minHeap of size k
        # minHeap[0] = kth largest
        # minHeap[-1] = the 1st largest.
        
        # heapify nums 
        self.k = k 
        self.minHeap = nums
        heapq.heapify(self.minHeap) 

        # keep popping off the smallest until there are only k items left        
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) 
    
    def add(self, val: int) -> int:
        
        # add this val to the heap 
        heapq.heappush(self.minHeap, val)

        # pop off the k+1th largest
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0] # return the kth largest 
        
