class KthLargest:

    # [3, [6, 7, 8]]

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums) # pop the first (smallest) number off. 
        # since our heap is of size k, we know heap[0] is the kth largest. 

    # adds val to the stream and returns the kth largest integer in the stream. 
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums) # pop the largest number off 
        return self.nums[0]

        
