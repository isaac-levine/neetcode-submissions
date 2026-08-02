class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0 
        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(m - 1, -1, -1):
            new = [0] * (n + 1) 
            new[n] = 1
            for j in range(n - 1, -1, -1):
                new[j] += dp[j] # skip
                if s[i] == t[j]:
                    new[j] += dp[j + 1] # use 
            dp = new
        
        return dp[0]