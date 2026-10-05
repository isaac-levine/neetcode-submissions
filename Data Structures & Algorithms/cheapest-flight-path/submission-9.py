class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # given list of directed weighted edges
        
        # cheapest path with at-most k BFS layers away -> Khan's? is that what its called? 
        # it's whichever algorithm where you do for i in range (k)

        # no yeah I think that's it and then you do union-find? 
        # but then how do you keep track of the actual cost? 

        # im not sure if its union find, I think the union find one is bellman-ford, and I don't
        # remember what Bellman Ford is used for....

        # actually i dont think its the union find one, i think it's something else where we 
        # process one BFS layer at a time 
        # omg yes and we maintain a prices[] that we copy at every layer. 

        prices = [float("inf")] * n
        prices[src] = 0
        for i in range(k + 1):
            newPrices = prices[::] # make a copy so we don't accidentally read our own new writes

            # process every edge for every layer
            for u, v, w in flights:
                if prices[u] != float("inf"): # from_i is reachable 
                    newPrices[v] = min(newPrices[v], (w + prices[u])) # update to_i with best price 

            prices = newPrices
        

        return prices[dst] if prices[dst] != float("inf") else -1