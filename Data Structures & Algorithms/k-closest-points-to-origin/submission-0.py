class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = [] 
        for x, y in points:
            d = self.distance(x, y)
            heapq.heappush(heap, (d, [x, y]))

        res = [] 
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res


    def distance(self, x, y):
        return math.sqrt((x ** 2) + (y ** 2))