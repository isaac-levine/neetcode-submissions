class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        N = len(grid)
        visit = set()
        minHeap = [[grid[0][0], 0, 0]] # (max-height, r, c)
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        # build adj 


        visit.add((0, 0))
        while minHeap:
            h, r, c = heapq.heappop(minHeap)
            if r == N - 1 and c == N - 1:
                return h
            
            for dr, dc in directions:
                r2, c2 = r + dr, c + dc
                if (r2 < 0 or c2 < 0 or r2 == N or c2 == N or (r2, c2) in visit):
                    continue
                visit.add((r2, c2))
                heapq.heappush(minHeap, [max(h, grid[r2][c2]), r2, c2])
            
