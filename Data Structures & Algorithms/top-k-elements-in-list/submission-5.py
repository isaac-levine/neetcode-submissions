class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # return the k most frequent elements of nums
        freq = Counter(nums) 
        
        # heapify 
        # O(n log n) 
        heap = [(-value, key) for key, value in freq.items()]
        heapq.heapify(heap)


        res = []
        for _ in range(k):
            count, num = heapq.heappop(heap)
            res.append(num)

        return res