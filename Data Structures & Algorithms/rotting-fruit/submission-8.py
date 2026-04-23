class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # multi-source BFS
        q = deque() 
        ROWS, COLS = len(grid), len(grid[0])
        minutesPassed = 0 
        fresh = 0
        directions = [[1,0], [-1,0], [0,1], [0, -1]]

        # start the queue with all the rotten fruits 
        # and count all the fresh fruits that we see. (so we know how many have to rot)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2: # rotten
                    q.append((r, c))
                elif grid[r][c] == 1: # count the number of fresh fruits initially
                    fresh += 1

        if fresh == 0:
            return 0 

        while q and fresh > 0:
            minutesPassed += 1 # increment minutesPassed here, instead of after because we will break as soon as fresh == 0

            for _ in range(len(q)): # take snapshot of queue size
                r, c = q.popleft() # pop off the top position from the queue 

                # check for out of bounds or empty tile 
                if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                    continue 

                # if it's fresh, make it rotten, decrement fresh count 
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    fresh -= 1
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1:
                        continue
                    else:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            

        return minutesPassed if fresh == 0 else -1 
        