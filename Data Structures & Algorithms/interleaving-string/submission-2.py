class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp, prev = [False] * (len(s2)+1), [False] * (len(s2)+1)

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                dp[j] = False
                if i == len(s1) and j == len(s2):
                    dp[j] = True
                if i < len(s1) and s1[i] == s3[i + j] and prev[j]:
                    dp[j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[j+1]:
                    dp[j] = True
            dp, prev = prev, dp

        return prev[0]
        