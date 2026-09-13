class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1): # if we're allowed to take k stops, that means we're allowed k + 1 edge layers away from src
            temp_prices = prices[::]

            for s, d, p in flights:
                if prices[s] != float("inf") and temp_prices[d] > prices[s] + p:
                    temp_prices[d] = prices[s] + p
            
            prices = temp_prices
        
        return prices[dst] if prices[dst] != float("inf") else -1


