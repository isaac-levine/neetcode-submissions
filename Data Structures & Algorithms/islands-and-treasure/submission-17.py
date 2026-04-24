class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        WATER, TREASURE, LAND = -1, 0, 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1,0], [-1,0], [0,1], [0,-1]]
        visit = set()
        distance = 0 

        # fill each land cell with the distance to its nearest treasure
        # must be reachable by land 
        # return the modified grid 

        # multi-source BFS. From each treasure chest, where we keep track of distance like minutes 
        
        # queue up the treasure chests as the starting positions for our BFS
        q = deque() 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == TREASURE:
                    q.append((r, c))
                    visit.add((r, c))

        while q: # 
            distance += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == LAND and (nr, nc) not in visit):
                        q.append((nr, nc))
                        visit.add((nr, nc))
                        grid[nr][nc] = distance
            
            
