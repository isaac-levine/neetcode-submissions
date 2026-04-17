class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set() 

        def enqueueCell(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] == -1:
                return
            q.append((r, c))
            visit.add((r, c))

            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0: # treasure chest
                    q.append((r, c))
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)): # go through the current snapshot of the queue 
                r, c = q.popleft()
                grid[r][c] = dist # update the distance 
                enqueueCell(r + 1, c)
                enqueueCell(r - 1, c)
                enqueueCell(r, c + 1)
                enqueueCell(r, c - 1)
            dist += 1


