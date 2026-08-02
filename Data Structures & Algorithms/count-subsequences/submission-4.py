class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        

        # number of distinct subsequences of s which are equal to t

        # for every subsequence you're trying to build, you can skip a character in s or use it.

        #   c a t
        # c 3
        # a   3
        # a   2
        # a   1
        # t     1
        #.        1 
        # going diagonal doesn't += 1 because 

        # if you use it, you have to advance to the next index j in t
        # if you don't use it, you have to stay at this index j in t. 


        # dp[i][j] = number of ways to form t[j:] using s[i:]

        #   x y 
        # x 5 5 1
        # x 1 4 1
        # y 1 3 1
        # x 1 2 1
        # y 0 1 1

        m, n = len(s), len(t)
        if m < n:
            return 0 
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m + 1):
            dp[r][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] += dp[i + 1][j] # skip
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1] # use 
                
        
        return dp[0][0]