class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # off bat I know it's DP 

        #   . b
        # a F F F
        # a F F F
        #   F F T 
        
        m, n = len(s), len(p)
        dp = [False] * (n + 1)

        for i in range(m, -1, -1):
            newDp = [False] * (n + 1)
            if i == m:
                newDp[n] = True
            for j in range(n - 1, -1, -1):
                if p[j] == "*":
                    continue 
                firstMatch = i < m and p[j] in (s[i], ".")
                
                # if next in p is a "*"
                if j < (n - 1) and p[j + 1] == "*":
                    if firstMatch:
                        newDp[j] = dp[j] or newDp[j + 2]
                    else:
                        newDp[j] = newDp[j + 2] 
                else:
                    newDp[j] = firstMatch and dp[j + 1]

            dp = newDp

        return dp[0]
                




