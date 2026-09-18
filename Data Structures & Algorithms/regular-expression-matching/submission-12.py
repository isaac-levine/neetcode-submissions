class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # off bat: this is definitely 2d dp again with two sequences as the rows and columns 

        # we definitely want some sort of firstMatch boolean lol im remembering the implementation shape a bit in my head

        # dp[i][j] = whether s[i:] can be made from p[j:]

        #   . b
        # a.  F
        # a   F
        # 

        # as we're moving backwards we can just skip over * and deal with them once we figure out what character it is

        #   n *
        # n
        # n
        # n T F F
        #       T

        # when we hit a *, either we skip it or we use it (first has to match a/.) meaning first has to match and we take 
        # the one directly below where we can decide to use it again or skip it at that point (future )

        # skipping it means we take whatever is to two the right

        #   . * z
        # x T   F F
        # y T   F F
        # z T   T F
        #   F F   T

        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[len(s)][len(p)] = True

        for r in range(len(s), -1, -1): # s -- string
            for c in range(len(p) - 1, -1, -1): # p -- pattern
                if p[c] == "*":
                    continue 

                firstMatch = r < len(s) and p[c] in (".", s[r])
                
                if c < len(p) - 1 and p[c + 1] == "*":
                    # star.
                    # can either use it if firstMatch or skip it
                    dp[r][c] = firstMatch and dp[r + 1][c] or dp[r][c + 2]
                else:
                    dp[r][c] = firstMatch and dp[r + 1][c + 1]


        return dp[0][0]
