class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        # minimum spanning tree -> like dijkstra's but with the edge not total cost
        # greedy BFS with minHeap but just using the edge cost

        res = 0 
        minHeap = [(0, points[0][0], points[0][1])] # (cost, x, y)
        visited = set() 

        while len(visited) < len(points):
            d, x, y = heapq.heappop(minHeap)
            if (x, y) in visited:
                continue 
            visited.add((x, y))
            res += d

            for neiX, neiY in points:
                if (neiX, neiY) not in visited:
                    dist = abs(x - neiX) + abs(y - neiY)
                    heapq.heappush(minHeap, (dist, neiX, neiY))

        return res
