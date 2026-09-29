class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # off bat i remember this being dijkstra's INSTEAD of prims based on past mistakes I think
        # actually wait...minimum cost to connect all points means minimum total cost -- we just need them all to be connected we 
        # minimum total wire cost laid down...,..if im understanding correctly...

        # and since we have all the points, not a stream of edges or anything like that, we should just use prim's 

        # which is just Dijkstra's but with the single edge weight (w) and Dijkstra's is just a greedy BFS with a heap 

        # surely its MST and not Dijkstra's right?

        minHeap = [(0, points[0][0], points[0][1])]
        visited = set() 
        cost = 0

        while minHeap:
            w, x, y = heapq.heappop(minHeap)
            if (x, y) in visited:
                continue 

            visited.add((x, y))
            cost += w
            print("adding cost: ", w, " from node: (", x, ",", y, ")")

            for a, b in points:
                if (a, b) not in visited:
                    edgeCost = abs(a - x) + abs(b - y)
                    heapq.heappush(minHeap, (edgeCost, a, b))
        
        return cost