class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        ROWS, COLS = m, n
        prevRow = [0] * COLS 
        for r in range(ROWS - 1, -1, -1):
            curRow = [0] * COLS 
            curRow[COLS - 1] = 1
            for c in range(COLS - 2, -1, -1):
                curRow[c] = curRow[c + 1] + prevRow[c]
            prevRow = curRow 
        
        return prevRow[0]
