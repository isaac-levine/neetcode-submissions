class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # This is the full dp[][] solution
        # dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        # ROWS, COLS = len(text1), len(text2)

        # for r in range(ROWS - 1, -1, -1):
        #     for c in range(COLS - 1, -1, -1):
        #         if text1[r] == text2[c]:
        #             dp[r][c] = 1 + dp[r + 1][c + 1]
        #         else:
        #             dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])
        
        # return dp[0][0]

        # This is simply the prevRow solution. (optimized space)
        ROWS, COLS = len(text1), len(text2)
        prevRow = [0] * (COLS + 1)

        for r in range(ROWS - 1, -1, -1):
            curRow = [0] * (COLS + 1)
            curRow[COLS] = 0 
            for c in range(COLS - 1, -1, -1):
                if text1[r] == text2[c]:
                    curRow[c] = 1 + prevRow[c + 1]
                else:
                    curRow[c] = max(prevRow[c], curRow[c + 1])

            prevRow = curRow

        return prevRow[0]
