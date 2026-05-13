class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # follow the simulation until there is one stone remaining and return its weight 

        heap = [-w for w in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x == y:
                continue
            else:
                diff = abs(x - y)
                heapq.heappush(heap, diff * -1)

        return heap[0] * -1 if heap else 0