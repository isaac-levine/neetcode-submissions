class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        # for each iteration of bfs, time += 1
        # if grid[r][c] <= time , then you can swim to that cell. 
        
        # from (0,0) minimum time it takes to reach bottom-right (n - 1, n - 1)

        # find minimum cost path from (0,0) to (n-1, n-1) and result is max in the path

        # is the normal greedy bfs approach of Dijkstra's enough to get us the right result? 


        # 1    1   1    1
        # 10  10. 100.  100
        # 2.  3    4.    5

        # this is a counterexample, so you cannot do simple dijkstra's because you might end up eventually adding more cost. 

        # normal dijkstra's uses sum of the costs of the path 
        # what single number determines when you can swim in a path though? the max.

        # idea: use the pathMax as the dijkstra's minHeap.

        minHeap = [(grid[0][0], 0, 0)] # (pathMax, (i,j))
        visit = set()

        while minHeap:
            pathMax, r, c = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue
            if r == n - 1 and c == n - 1:
                return pathMax

            visit.add((r, c))

            # push neighboring nodes with updated path max.
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nc >= 0 and nr < n and nc < n and (nr, nc) not in visit:
                    heapq.heappush(minHeap, (max(pathMax, grid[nr][nc]), nr, nc))



