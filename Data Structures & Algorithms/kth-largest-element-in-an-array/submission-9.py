class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [n * -1 for n in nums]
        heapq.heapify(maxHeap)

        res = maxHeap[0] * -1 
        while k:
            res = heapq.heappop(maxHeap) * -1
            k -= 1
        return res 
