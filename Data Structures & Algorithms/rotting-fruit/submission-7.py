class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        num_fresh_fruits = 0 
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        # count the number of fresh fruits in the grid initially
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num_fresh_fruits += 1
                elif grid[r][c] == 2:
                    q.append((r, c)) # set up the initial positions 
        
        if num_fresh_fruits == 0:
            return 0

        def enqueue_cell(r, c):
            nonlocal num_fresh_fruits
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1: # out of bounds or not fresh fruit 
                return
            grid[r][c] = 2
            num_fresh_fruits -= 1
            q.append((r, c))


        # multi-source BFS from the rotten fruits 
        minute = 0
        while q and num_fresh_fruits > 0:
            
            for _ in range(len(q)):
                r, c = q.popleft() 

                # infect all the fresh fruits in all four directions from here
                enqueue_cell(r + 1, c)
                enqueue_cell(r - 1, c)
                enqueue_cell(r, c + 1)
                enqueue_cell(r, c - 1)
            
            minute += 1
            
        
        return minute if num_fresh_fruits <= 0 else -1 
