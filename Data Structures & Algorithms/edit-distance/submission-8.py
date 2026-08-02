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
        dp = list(range(COLS, -1, -1))

        # build the bottom row (you would have to delete every character)
        for c in range(COLS):
            dp[c] = COLS - c


        for i in range(ROWS - 1, -1, -1):
            cur = [0] * (COLS + 1) 
            cur[COLS] = ROWS - i
            for j in range(COLS - 1, -1, -1):
                if word2[i] == word1[j]:
                    cur[j] = dp[j + 1]
                else:
                    cur[j] = 1 + min(
                        dp[j], # insert, move to the next character in word2
                        cur[j + 1], # delete, move to the next character in word1
                        dp[j + 1], # replace, move to the next character in both
                    )
            dp = cur

        return dp[0]