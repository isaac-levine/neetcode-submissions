class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        # we're optimizing for the minimum maxPathHeight
        minHeap = [(grid[0][0], 0, 0)] # (maxPathHeight, r, c)
        visited = set() 
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        n = len(grid)

        while True: # we will just hard break, since we know there is a valid solution 

            maxPathHeight, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue

            if r == n - 1 and c == n - 1:
                return maxPathHeight

            visited.add((r, c))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # push in bounds, unvisited, and valid height neighbors
                if (nr < 0 or nc < 0 or nr >= n or nc >= n or (nr, nc) in visited):
                    continue 
                heapq.heappush(minHeap, (max(maxPathHeight, grid[nr][nc]), nr, nc))
                

            
