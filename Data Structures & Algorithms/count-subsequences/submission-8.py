class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # def dfs(i, j)

        # What is my recursive decision? --> Use or skip this s[i]
        # What do I need to remember about those decisions? --> i and j, where i is position in s and j is position in t
        # This is probably a pull, because we know at the end of the array is a base case that we can build off. 
        # What are my base cases? --> There 
        # What is the reccurence? --> num ways when you skip + num ways when you use it. 
        #                           = dfs(i + 1, j) (skip it) + dfs(i + 1, j + 1) (use it)


        # dp[i][j] = number of distcint subsequences of t[j:] in s[i:]
        # rows --> s
        # cols --> t

        # s = "caaat", t = "cat"
        #   c a t 
        # c 3 3 1 1
        # a 0 3 1 1
        # a 0 2 1 1
        # a 0 1 1 1
        # t 0 0 1 1
        #   0 0 0 1

        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        for r in range(len(s) + 1):
            dp[r][len(t)] = 1 # there is exactly 1 way to build "", no matter what you have. you just skip everything. 
            # the rightmost column is all 1's.

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                
                dp[i][j] += dp[i + 1][j] # skip this s[i]
                # or use this s[i] if the character's match
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        
        return dp[0][0]

