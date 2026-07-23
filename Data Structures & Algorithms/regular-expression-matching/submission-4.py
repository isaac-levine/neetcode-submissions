class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        

        # dp[i][j] represents whether the substrings s[i:] and p[j:] match
        # p (cols) =    . b _
        # s (rows)     a 
        #              a
        #              _.   True
        m, n = len(s), len(p)
        prev = [False] * (n + 1)
        prev[n] = True 

        for i in range(m, -1, -1): # compute bottom row
            curr = [False] * (n + 1)
            curr[n] = i == m # can only make empty string with empty pattern (bottom-right)
            for j in range(n - 1, -1, -1):
                firstMatch = i < m and p[j] in ('.', s[i]) # "." or match
                # if the next p[j + 1] is a star 
                    # use it: you just need s[i + 1] to match p[j] and firstMatch 
                    # OR 
                    # skip it: dp[i][j + 2]
                if (j + 1) < n and p[j + 1] == '*':
                    curr[j] = curr[j + 2] or (firstMatch and prev[j])
                else: # else rely on firstMatch and dp[i + 1][j + 1]
                    curr[j] = firstMatch and prev[j + 1]
            
            prev = curr 
        
        return curr[0]
