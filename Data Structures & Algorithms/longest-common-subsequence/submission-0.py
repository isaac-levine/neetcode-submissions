class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]
        ROWS = len(text1)
        COLS = len(text2)
        # COLS = # in text1
        # ROWS = # in text2

        # loop through every cell
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r+1][c+1] # 1 + the diagonal if they match
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1]) # max of right and down if they dont
        
        return dp[0][0]
                