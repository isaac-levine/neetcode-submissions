class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # off bat I know it's DP 

        #   . b
        # a F F F
        # a F F F
        #   F F T 
        
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                if p[j] == "*":
                    continue 
                firstMatch = i < m and p[j] in (s[i], ".")
                
                # if next in p is a "*"
                if j < (n - 1) and p[j + 1] == "*":
                    if firstMatch:
                        dp[i][j] = dp[i + 1][j] or dp[i][j + 2]
                    else:
                        dp[i][j] = dp[i][j + 2] 
                else:
                    dp[i][j] = firstMatch and dp[i + 1][j + 1]

        return dp[0][0]
                




