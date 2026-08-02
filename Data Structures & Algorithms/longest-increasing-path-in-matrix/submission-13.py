class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        # Grid DP.

        # You can move in any direction 
        
        # What is my recursive atomic decision? --> which direction to move (up/down/left/right)
        # What do I need to remember about it (state)? --> what the position was (i, j)
        # Push or pull? --> not sure that it matters?
        # What is the recurrence? --> LIP[i][j] = if any of the neighbors are > me. 1 + max(neighbors)
        # Base cases? --> if you make an extra ring around the outside. i think it would be all zeros.

        # But you run into a problem: how do you know where to start without using recursion? --> Just sort the cells by value and process the biggest ones 
        # first (and then use a pull)

        # 0 0 1
        # 2 1 0 
        # 3 2 1

        ROWS, COLS = len(matrix), len(matrix[0])

        dp = {} # (r,c) -> LIP

        def dfs(r, c, prev):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or matrix[r][c] <= prev:
                return 0 # out of bounds or this path is no longer increasing
            elif (r, c) in dp:
                return dp[(r, c)] # this position has already been computed and cached
            
            dp[(r, c)] = 1 + max(
                dfs(r + 1, c, matrix[r][c]),
                dfs(r - 1, c, matrix[r][c]),
                dfs(r, c + 1, matrix[r][c]),
                dfs(r, c - 1, matrix[r][c])
            )
            return dp[(r, c)]

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, -1))
        return res