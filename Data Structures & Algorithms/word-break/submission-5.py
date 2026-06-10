class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        dp = [False] * (len(s) + 1) # starting at dp[i] / s[i], can you make it to the end with valid words?  
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) < len(dp) and dp[i + len(word)] and s[i:i+len(word)] == word:
                    dp[i] = True

        return dp[0]




