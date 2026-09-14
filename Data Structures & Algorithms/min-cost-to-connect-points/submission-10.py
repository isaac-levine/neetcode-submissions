class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # off bat thoughts: canonical MST problem?
        # lets do prims..dijkstra's but with just the edge weight not total path weight 
        # wait no but we only have points, so technically we have edges between everything 

        minHeap = [(0, points[0][0], points[0][1])] 

        adj = defaultdict(list)
        visited = set() 
        minCost = 0
        
        def dist(x1, y1, x2, y2):
            return (abs(x1 - x2)) + (abs(y1 - y2))

        while minHeap:
            cost, x, y = heapq.heappop(minHeap)
            if (x, y) in visited:
                continue 
            minCost += cost
            visited.add((x, y))

            for neiX, neiY in points:
                if (neiX, neiY) not in visited:
                    d = dist(x, y, neiX, neiY)
                    heapq.heappush(minHeap, (d, neiX, neiY)) # push unvisited neighbors with total path cost

        return minCost