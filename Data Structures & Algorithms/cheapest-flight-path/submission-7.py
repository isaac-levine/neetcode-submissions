class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # cheapest path from src to desk going through at most k nodes -- -1 if impossible. 
        # weighted cheapest path from src to dest -> dijkstra's 
        # but how do we handle k?

        # here, using float("inf") as a sentinenal makes sense when considering min cost

        # we know n is small and prices are small 
        prev_prices = [float("inf")] * n
        prev_prices[src] = 0

        for i in range(k + 1): # allowed to make k stops at most 
            # i represents the layer/number of stops away from src 
            # so first iteration is what's reachable from i == 0 stops away i.e. reachable from src
            
            # check every edge every time 
            new_prices = prev_prices[:]
            for s, d, p in flights:
                # if source is previously reachable, try updating new destination price
                if prev_prices[s] != float("inf") and new_prices[d] > (prev_prices[s] + p):
                    new_prices[d] = prev_prices[s] + p
            prev_prices = new_prices

        return prev_prices[dst] if prev_prices[dst] != float("inf") else -1



