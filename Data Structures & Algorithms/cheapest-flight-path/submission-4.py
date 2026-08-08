class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        prices = [float("inf")] * n
        prices[src] = 0 

        for i in range(k + 1): # k layers
            tempPrices = prices.copy() 

            for s, d, p in flights: # iterate through each edge (source, dest, price)
                if prices[s] == float("inf"): # we can't even reach this source node
                    continue
                tempPrices[d] = min(tempPrices[d], prices[s] + p)
        
            prices = tempPrices
        
        return prices[dst] if prices[dst] != float("inf") else -1 