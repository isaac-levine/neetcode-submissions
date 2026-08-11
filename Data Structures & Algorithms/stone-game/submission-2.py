class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        # len(piles) - even -- they get same number of piles 
        # sum(piles) - odd -- someone wins
        # so really alice always wins -- can just return True lol. 

        # greedy -> commit to local best decision and can't undo it. 


        dp = {} # (l, r) : max score alice can get for this interval

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            even = (r - l + 1) % 2 == 0 # only alice's turn on even turns
            leftMost = piles[l] if even else 0 
            rightMost = piles[r] if even else 0 
            # max of taking the left and taking the right 
            dp[(l, r)] = max(leftMost + dfs(l + 1, r), rightMost + dfs(l, r - 1))
            return dp[(l, r)]

        maxAliceScore = dfs(0, len(piles) - 1)
        total = sum(piles)
        return maxAliceScore > total - maxAliceScore