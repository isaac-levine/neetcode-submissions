class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # [2,3,1,1,5,5,4]
        #.       ^
        # k = 3

        minHeap = []  # 1,2,3

        for num in nums:
            if len(minHeap) == k and minHeap[0] >= num:
                continue # skip if we already have size-k heap and this num is not larger than current kth largest
            elif len(minHeap) == k and num > minHeap[0]:
                heapq.heappop(minHeap) # pop the top off if it is size-k and current kth largest is smaller 
            heapq.heappush(minHeap, num)

        
        return minHeap[0]