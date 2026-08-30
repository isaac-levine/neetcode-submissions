class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # i know this is 2d dp off memory

        # dp[i][j] = # of distinct subsequences of s[i:] that are equal to t[j:]

        m, n = len(s), len(t) 

        #   c a t _
        # c 3 3 1 0
        # a 0 3 1 0
        # a 0 2 1 0
        # a 0 1 1 0
        # t 0 0 1 0
        # _ 0 0 0 1  


        #   x y   
        # x 3 1 1
        # x 2 1 1
        # y 1 1 1
        # x 1 1 1
        # y 0 1 1
        #   0 0 1

        # characters match --> dp[i][j] = dp[i + 1][j + 1] (using this one) + dp[i + 1][j] (not using this)
        # characters don't match --> dp[i + 1][j] (don't use this )
        # if t is longer than s, move on 


        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = 1
        for r in range(m + 1):
            dp[r][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]: 
                    # match, can either use this s[i] or I can skip it 
                    dp[i][j] = dp[i + 1][j] + dp[i + 1][j + 1]
                else: 
                    # don't match, have to just skip 
                    dp[i][j] = dp[i + 1][j] 

        
        return dp[0][0]