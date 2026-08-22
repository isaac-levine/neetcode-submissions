class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        # going from src (0,0) to dest (n - 1, n - 1) --> bfs/dijkstra's/bellman-ford family 

        # optimize for max height seen so far.
        # and for each layer of BFS just increase time 

        # so use dijkstra's for shortest path, but instead of cost use maxHeightSeenSofar.
        # there is no egde cost between things, just time and worst case height

        
        minHeap = [(grid[0][0], 0, 0)] # (maxSeenHeight, (r, c))
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        n = len(grid)
        visited = set()

        while minHeap:
            maxHeight, r, c = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue
            # early return instead of using a res because we might not visit every node and that's fine 
            if r == n - 1 and c == n - 1:
                return maxHeight

            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= n or nc >= n or (nr, nc) in visited:
                    continue
                heapq.heappush(minHeap, (max(maxHeight, grid[nr][nc]), nr, nc))

         