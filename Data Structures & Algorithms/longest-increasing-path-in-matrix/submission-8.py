class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[-1] * COLS for _ in range(ROWS)]

        def dfs(i, j, prev):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or matrix[i][j] <= prev:
                return 0  # out of bands or not increasing 
            if dp[i][j] > -1:
                return dp[i][j]

            dp[i][j] = 1 + max (
                dfs(i + 1, j, matrix[i][j]),
                dfs(i - 1, j, matrix[i][j]),
                dfs(i, j + 1, matrix[i][j]),
                dfs(i, j - 1, matrix[i][j])
            )

            return dp[i][j]

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, -1)) # the LIP can begin at any position
        return res
