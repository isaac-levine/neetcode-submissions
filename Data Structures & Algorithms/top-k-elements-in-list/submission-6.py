class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1

        heap = [(-value, key) for key, value in counts.items()]
        # heapq.heapify(heap)

        # res = [] 
        # for i in range(k):
        #    _, key = heapq.heappop(heap) 
        #    res.append(key)

        
        # can actually replace lines the heapify all the way down to the result building with: 
        kLargest = heapq.nsmallest(k, heap) 
        return [k for v, k in kLargest]


        # return res
