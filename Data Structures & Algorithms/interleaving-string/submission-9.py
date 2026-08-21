class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        

        # if you interleave, by definition the abs(cutsN - cutsM) will be <= 1 i think... 

        if len(s3) != len(s1) + len(s2):
            return False
        

        # aac
        # abc
        # aabacc

        # i think it's dynamic programming because the backtracking would get really freaky and clean 2-pointer wouldn't work 

        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)] 
        dp[m][n] = True
        # can you build s3[i+j:] using s1[i:] and s2[j:]
        #   a a a a _
        # b
        # b
        # b
        # b.      T 
        # _ T T T T T

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                # use s1[i], move to next i in s1
                if i < m and s1[i] == s3[i + j]:
                    dp[i][j] |= dp[i + 1][j]
                if j < n and s2[j] == s3[i + j]:
                    dp[i][j] |= dp[i][j + 1]

        return dp[0][0]
                