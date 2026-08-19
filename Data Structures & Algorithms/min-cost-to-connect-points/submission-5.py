class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        # minimum spanning tree -> like dijkstra's but with the edge not total cost
        # greedy BFS with minHeap but just using the edge cost

        res = 0 
        minHeap = [(0, 0)] # (cost, index)
        visited = set() # indeces that we have visted 

        while len(visited) < len(points):
            d, i = heapq.heappop(minHeap)
            # this is the only exit door out of the heap, so since we can't 
            # delete from the middle of the heap, we just have to check validity at exit 
            if i in visited: # is this offer still valid? 
                continue 
            visited.add(i)
            res += d

            for j in range(len(points)):
                if j not in visited: # save some pushes, but still need to check later
                    neiX, neiY = points[j]
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(minHeap, (dist, j))

        return res
