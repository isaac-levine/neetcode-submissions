class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        # elevation must be <= time in order to move there. 

        # source to destination -> BFS 
        # we can increment time at each layer. 

        # or...another way to think about minimum amount of time to reach end pos. is
        # by minimax the paths to get there. so you want the minimum maxPathHeight
        
        # dijkstra's but with maxPathHeight instead of the pathCost. 
        # and then you don't even have to simulate the time at all 

        minHeap = [(grid[0][0], 0, 0)] # (h, r, c) -- # [(2,1,0), (3,1,1)]
        visit = set() # (0,0), (0,1)
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        n = len(grid)

        while minHeap:
            maxPathHeight, r, c = heapq.heappop(minHeap)
            if (r, c) in visit: # have to check both at pop and push time b/c you don't know when different positions will get processed and visited. also because its possible for positions to get double-pushed actually i think. 
                continue 
            if r == n - 1 and c == n - 1:
                return maxPathHeight

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in visit or nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue
                heapq.heappush(minHeap, (max(maxPathHeight, grid[nr][nc]), nr, nc)) # update max at push time

            visit.add((r, c))
        
        return -1 