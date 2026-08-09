class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        # prim's is just dijkstra's but with the edge cost instead of totalCost. 

        # the cost between src and dest is the manhattan distance 

        # we need the MST cost starting from (0, 0)

        res = 0
        minHeap = [(0, 0)] # cost, x, y
        visit = set() 

        while minHeap:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue

            res += cost
            visit.add(i)

            for j in range(len(points)):
                if j not in visit:
                    heapq.heappush(minHeap, ((abs(points[i][0] - points[j][0])) + abs(points[i][1] - points[j][1]), j))

        return res

