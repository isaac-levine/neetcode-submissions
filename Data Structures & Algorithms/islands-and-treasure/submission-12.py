class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0, -1]]
        INF = 2147483647
        visit = set()
        q = deque()

        # Add all treasure chests to the queue to start
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0: # treasure chest
                    q.append((r, c)) 
                    visit.add((r, c))

        dist = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                grid[x][y] = dist
                for dr, dc in directions:
                    r, c = x + dr, y + dc
                    if not (min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in visit or grid[r][c] == -1):
                        q.append((r, c))
                        visit.add((r, c))
                    

            dist += 1


                
