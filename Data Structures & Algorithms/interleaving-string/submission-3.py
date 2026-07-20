class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True

        # dp[i][j] = can s3[i+j:] be formed using s1[i:] and s2[j:]
        # depends on dp[i + 1][j] (s1[i:]) (below) and dp[i][j + 1] (s2[j:]) (right)

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if (
                    (i < m and dp[i + 1][j] and s1[i] == s3[i + j]) or
                    (j < n and dp[i][j + 1] and s2[j] == s3[i + j])
                ):
                    dp[i][j] = True
        
        return dp[0][0]
