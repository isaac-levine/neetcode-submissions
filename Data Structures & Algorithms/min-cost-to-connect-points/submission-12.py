class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        # MST -- minimum total cost of laying down the wire. and it doesnt matter which point you start from. 
        # we have all the points, and they connect to all other points (all hypothetical edges are possible) so I think it's just Prim's -- the default MST algorithm....

        minHeap = [(0, 0)] # (w, i) where   w = edge cost
        #                                   i = points index


        visited = set()
        res = 0
        
        while minHeap:
            w, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            visited.add(i)
            res += w
            
            for j in range(len(points)):
                if j not in visited:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(minHeap, (dist, j))

        return res