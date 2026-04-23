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

            for _ in range(len(q)): # take snapshot of queue size
                r, c = q.popleft() # pop off the top position from the queue 

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        # do all the work of making it rotten at enqueue-time 
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1

            minutesPassed += 1

        return minutesPassed if fresh == 0 else -1 
        