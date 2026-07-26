class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)

        for i in range(m - 1, -1, -1): # rows correspond to text1
            cur = [0] * (n + 1)
            for j in range(n - 1, -1, -1): # cols correspond to text2
                
                # case 1: the letters are the same, move diagonal
                if text1[i] == text2[j]:
                    cur[j] = 1 + dp[j + 1]
                else:
                # case 2: skip to the right
                # case 3: skip down
                    cur[j] = max(dp[j], cur[j + 1])
            dp = cur
        
        return dp[0]