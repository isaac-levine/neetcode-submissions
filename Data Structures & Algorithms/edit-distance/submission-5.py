class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m, n = len(word2), len(word1)
        dp = list(range(n, -1, -1))

        for i in range(m - 1, -1, -1):
            cur = [0] * (n + 1)
            cur[n] = m - i # set the rightmost column increasing from 0 in bottom corner, up to m
            for j in range(n - 1, -1, -1):
                if word2[i] == word1[j]: # do nothing
                    cur[j] = dp[j + 1]
                else:
                    cur[j] = 1 + min( # operation 
                        dp[j], # insert
                        cur[j + 1], # delete
                        dp[j + 1] # replace
                    )
            dp = cur 
        
        return dp[0]

        