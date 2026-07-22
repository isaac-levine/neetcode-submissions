class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        if not word1:
            return len(word2)
        elif not word2:
            return len(word1)


        #   m o n k e y s  (word1 ) n cols, 
        # m               5
        # o               4
        # n               3 
        # e               2
        # y             1 1
        #   7 6 5 4 3 2 1 0

        # word2, m rows 

        # if word2[i] == word1[j] -> dp[i][j] = dp[i + 1][j + 1] -- do nothing
        # else:
            # insert -- 1 + dp[i + 1][j] # j pointer in word1 does not move. but i moves to next character of word2. 
            # delete -- 1 + dp[i][j + 1] # 1 pointer in word2 does not move. but j moves to next character of word1 
            # replace -- 1 + dp[i + 1][j + 1]

        m, n = len(word2), len(word1)
        dp = list(range(n, -1, -1))

        # len(word2) (m) - row. 


        for i in range(m - 1, -1, -1):
            cur = [0] * (n + 1)
            cur[n] = m - i 
            for j in range(n - 1, -1, -1):
                if word2[i] == word1[j]: # do nothing
                    cur[j] = dp[j + 1]
                else:
                    cur[j] = 1 + min( # operation 
                        dp[j], # insert
                        cur[j + 1], # delete
                        dp[j + 1] # replace
                    )
            dp = cur 
        
        return dp[0]

        