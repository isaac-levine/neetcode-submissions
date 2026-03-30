class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # all nodes have price infinity except for 0 to get to src node
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()  # whatever prices is at this time

            for s, d, p in flights: # s = src, d = dest, p = price
                if prices[s] == float("inf"):
                    continue # not possible to reach this
                if prices[s] + p < tmpPrices[d]: # check tmpPrices because if we update multiple times, we want to make sure that's reflected
                    tmpPrices[d] = prices[s] + p

            prices = tmpPrices

        return prices[dst] if prices[dst] != float("inf") else -1

            