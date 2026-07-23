class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        

        # dp[i][j] represents whether the substrings s[i:] and p[j:] match
        # p (cols) =    . b _
        # s (rows)     a 
        #              a
        #              _.   True
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True 

        for i in range(m, -1, -1): # compute bottom row
            for j in range(n - 1, -1, -1):
                firstMatch = i < m and p[j] in ('.', s[i]) # "." or match
                # if the next p[j + 1] is a star 
                    # use it: you just need s[i + 1] to match p[j] and firstMatch 
                    # OR 
                    # skip it: dp[i][j + 2]
                if (j + 1) < n and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or (firstMatch and dp[i + 1][j])
                else: # else rely on firstMatch and dp[i + 1][j + 1]
                    dp[i][j] = firstMatch and dp[i + 1][j + 1]
        
        return dp[0][0]
