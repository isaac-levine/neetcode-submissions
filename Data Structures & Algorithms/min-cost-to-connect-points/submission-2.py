class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def cost(i: List[int], j: List[int]) -> int:
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        # return minimum total cost to connect all points together
        
        # the trick of this problem is the graph is complete: there's no setup to do
        # nodes = 0...n-1 in points[] 
        

        minHeap = [(0, 0)] # just (edge_weight, index) we don't care what the source was
        visited = set()
        totalCost = 0

        while minHeap:

            w, i = heapq.heappop(minHeap)
            if i in visited:
                continue 

            visited.add(i)
            totalCost += w 
            
            for j in range(len(points)):
                if j in visited:
                    continue
                heapq.heappush(minHeap, (cost(i, j), j))
        
        return totalCost 