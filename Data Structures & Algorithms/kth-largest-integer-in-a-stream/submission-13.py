class KthLargest:

    def __init__(self, k: int, nums: List[int]): # since nums is given to us unsorted, we have to add every num to the heap

        # we only need a minHeap of size k
        # minHeap[0] = kth largest.....the 1st largest is some other leaf node we don't know where....
        
        # heapify nums 
        self.k = k 
        self.minHeap = nums
        heapq.heapify(self.minHeap) 

        # keep popping off the smallest until there are only k items left        
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) # this pruning here is not strictly necessary -- can just prune at first add call
    
    def add(self, val: int) -> int:
        
        # add this val to the heap 
        heapq.heappush(self.minHeap, val)

        # pop off the k+1th largest
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0] # return the kth largest 
        
