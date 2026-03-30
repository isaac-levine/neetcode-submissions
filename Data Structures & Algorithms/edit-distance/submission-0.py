class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # base cases
        if len(word2) == 0:
            return len(word1)
        elif len(word1) == 0:
            return len(word2)

        dp =[[float("inf")] * (len(word2) + 1) for _ in range (len(word1) + 1)]
        # make rightmost column 3, 2, 1, 0
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i
        # make bottom row 3, 2, 1, 0
        dp[len(word1)] = [len(word2) - j for j in range(0, len(word2) + 1)]

        # 3 things to try
        # delete: move word1 pointer
        # insert: move word2 pointer
        # replace: move both 
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    # try 3 (all of these require adding an operation)
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
        return dp[0][0]
        
        