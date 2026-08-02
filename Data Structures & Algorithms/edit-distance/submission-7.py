class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # decision: what operation to make at this position on word1? or should i do nothing? (4 choices)
        # state: where are you in word1 (i) and where are you in word2? (j)
        # pull -> because base case
        # base case -> 0 operations needed to make "" (word1) become "" (word2)
        #           -> n operations for to make "" for any s[i:] of length n -- these are all removals. 
        # relation: 1 + min(insert, delete, replace) if the characters do not match, or just dp[i + 1][j + 1] if they do match. 


        #   m o n k e y s      ---- word1 (cols)
        # m               5 
        # o               4 
        # n               3
        # e               2
        # y     4 3 2 1 1 1
        #   7 6 5 4 3 2 1 0

        ROWS, COLS = len(word2), len(word1)
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        # build the bottom row (you would have to delete every character)
        for c in range(COLS):
            dp[ROWS][c] = COLS - c

        # build the rightmost column (you would have to insert every character)
        for r in range(ROWS):
            dp[r][COLS] = ROWS - r

        for i in range(ROWS -1, -1, -1):
            for j in range(COLS -1, -1, -1):
                if word2[i] == word1[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i + 1][j], # insert, move to the next character in word2
                        dp[i][j + 1], # delete, move to the next character in word1
                        dp[i + 1][j + 1], # replace, move to the next character in both
                    )

        return dp[0][0]