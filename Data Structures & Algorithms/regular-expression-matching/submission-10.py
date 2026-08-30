class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # I remember from title that this is a 2d DP problem...
        # also the words setup makes me think 2d grid dp

        # I think when traversing what you wanna do is go backwards and when you hit a *, just look for the character before it. i think you can assume the pattern is well-formed. 


        m, n = len(s), len(p)
        prev = [False] * (n + 1)
        prev[n] = True


        for r in range(len(s), -1, -1): # s -- string
            cur = [False] * (n + 1)
            if r == m:
                cur[n] = True
            for c in range(len(p) - 1, -1, -1): # p -- pattern
                charsMatch = r < len(s) and (p[c] in [".", s[r]])
                if c + 1 < len(p) and p[c + 1] == "*":
                    # star: either skip the star or use it at least once.
                    cur[c] = cur[c + 2] or (charsMatch and prev[c])
                else:
                    # no star: need . or match and then diagonal
                    cur[c] = charsMatch and prev[c + 1]

            prev = cur

        return prev[0]
                
