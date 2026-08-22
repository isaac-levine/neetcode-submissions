class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # cheapest path from src to desk going through at most k nodes -- -1 if impossible. 
        # weighted cheapest path from src to dest -> dijkstra's 
        # but how do we handle k?

        # here, using float("inf") as a sentinenal makes sense when considering min cost

        # we know n is small and prices are small 
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1): # allowed to make k stops at most 
            # i represents the layer/number of stops away from src 
            # so first iteration is what's reachable from i == 0 stops away i.e. reachable from src
            
            # check every edge every time 
            temp_prices = prices[:]
            for s, d, p in flights:
                # if src is already reachable, try updating dest price 
                # reachability check needs to read from prices 
                # comparison to dest price should reach from temp_prices though, so we update with the best
                if prices[s] != float("inf") and (prices[s] + p) < temp_prices[d]:
                    temp_prices[d] = prices[s] + p
            prices = temp_prices

        return prices[dst] if prices[dst] != float("inf") else -1



