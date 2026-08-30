class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # I remember from title that this is a 2d DP problem...
        # also the words setup makes me think 2d grid dp

        # I think when traversing what you wanna do is go backwards and when you hit a *, just look for the character before it. i think you can assume the pattern is well-formed. 


        #    n * _
        # n  T
        # n  T
        # n. T   
        # _. T   T <-- base case: empty pattern forms empty string 


        #   . b _
        # a F F
        # a F F
        # _     T


        # c + 1 == "*"
        # "." or characters match -> dp[r + 1][c + 1]
        # 
        

        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[len(s)][len(p)] = True

        for r in range(len(s), -1, -1):
            for c in range(len(p) - 1, -1, -1):
                charsMatch = r < len(s) and (p[c] in [".", s[r]])
                if c + 1 < len(p) and p[c + 1] == "*":
                    # star: either skip the star or use it at least once.
                    dp[r][c] = dp[r][c + 2] or (charsMatch and dp[r + 1][c])
                else:
                    # no star: need . or match and then diagonal
                    dp[r][c] = charsMatch and dp[r + 1][c + 1]

        return dp[0][0]
                
