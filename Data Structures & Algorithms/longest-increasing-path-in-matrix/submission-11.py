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
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # list of (r,c) pairs sorted by their value in matrix[r][c]
        sortedCells = sorted(((r, c) for r in range(ROWS) for c in range(COLS)), key = lambda rowCol : matrix[rowCol[0]][rowCol[1]])

        dp = [[0] * COLS for _ in range(ROWS)]

        for r, c in sortedCells: 
            # what is the longest increasing path ending here at position (r, c)?
            longest = 0 
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] < matrix[r][c]: # ending here so check for neighbors smaller.
                    longest = max(longest, dp[nr][nc])
            dp[r][c] = 1 + longest

        return max(max(row) for row in dp) # return the max of all the rowMaxes.
