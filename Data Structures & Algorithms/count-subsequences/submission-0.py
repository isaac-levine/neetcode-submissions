class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        cache = {} # (i,j) -> numDistinct

        def backtrack(i, j):
            # base cases
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i,j)]
            # recursive steps
            if s[i] == t[j]:
                return backtrack(i + 1, j + 1) + backtrack(i + 1, j)
            else:
                return backtrack(i + 1, j)

        return backtrack(0, 0)
        
        
            


       
        