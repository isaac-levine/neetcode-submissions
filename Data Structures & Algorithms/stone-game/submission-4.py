class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        dp = {} # (l, r) : best net advantage for whoever moves right now 

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            dp[(l, r)] = max(piles[l] - dfs(l + 1, r), 
                             piles[r] - dfs(l, r - 1))
            return dp[(l, r)]

        return dfs(0, len(piles) - 1) > 0 # if alice has net advantage 