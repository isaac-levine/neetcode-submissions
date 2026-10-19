class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # THE CONVENTION (pin this before any line of code):
        #   dp[a][c] = number of ways to make amount `a`
        #              using only the coin SUFFIX coins[c:]
        #              (coin c and everything to its right).
        #
        # So moving RIGHT in a row = having FEWER coins available.
        # The last column, dp[a][len(coins)], means "no coins at all."

        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]

        # SEED, read by meaning:
        # "How many ways to make amount 0?" -> exactly one (take nothing),
        # and that's true no matter which coin suffix you hold.
        # So the ENTIRE top row is 1 -- including dp[0][len(coins)]:
        # even with zero coins, making 0 works. That corner is what
        # eventually feeds every real answer.
        for c in range(len(coins) + 1):
            dp[0][c] = 1
        # (Everything else stays 0 -- including the whole "no coins"
        # column below row 0: with no coins you can't make a > 0.)

        for a in range(1, amount + 1):          # row by row, small amounts first
            for c in range(len(coins) - 1, -1, -1):   # RIGHT to LEFT within the row
                # Why right-to-left? The skip arm reads dp[a][c + 1],
                # one cell to the RIGHT in the SAME row. Going right-to-left
                # means that cell is already computed when we need it.
                # (Who am I allowed to read from? -- answered by direction.)

                coin = coins[c]

                # ARM 1 -- SKIP this coin entirely:
                # every way to make `a` without coin c is a way using
                # the smaller suffix coins[c+1:]. Same amount, one cell right.
                dp[a][c] += dp[a][c + 1]

                # ARM 2 -- USE this coin (at least once):
                # spend `coin` now; what remains is "make a - coin".
                # KEY: we stay in COLUMN c, not c+1 -- the coin is still
                # available after using it. That same-column read IS the
                # unbounded/reuse semantics. (Moving to c+1 here would
                # make each coin usable once -- the 0/1 knapsack.)
                # And we subtract the COIN'S VALUE, never the index c --
                # this row's twice-bitten token bug.
                if a >= coin:
                    dp[a][c] += dp[a - coin][c]
                # Note: dp[a - coin][c] is a SMALLER amount -> an earlier,
                # fully-finished row. Safe to read in any inner order.

        # ANSWER: the full suffix coins[0:] = all coins available.
        return dp[amount][0]