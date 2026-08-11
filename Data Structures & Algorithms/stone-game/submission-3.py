class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        # len(piles) - even -- they get same number of piles 
        # sum(piles) - odd -- someone wins
        # so really alice always wins -- can just return True lol. 

        # greedy -> commit to local best decision and can't undo it. 


        dp = {} # (l, r) : best net advantage for whoever moves right now 

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            # even = (r - l + 1) % 2 == 0 # only alice's turn on even turns
            # leftMost = piles[l] if even else 0 
            # rightMost = piles[r] if even else 0 
            # max of taking the left and taking the right 
            dp[(l, r)] = max(piles[l] - dfs(l + 1, r), 
                             piles[r] - dfs(l, r - 1))
            return dp[(l, r)]

        return dfs(0, len(piles) - 1) > 0 # if alice has net advantage 