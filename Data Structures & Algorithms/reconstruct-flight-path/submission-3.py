class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # each ticket is an edge
        # each edge was traversed exactly once 
        # path started from JFK 

        # starting from JFK, what is the lexicographically cheapest way to hit every airport?

        # we can revisit the same node multiple times, but not the same edge

        tickets.sort() # by default, will go to ticket[1] for sort order if ticket[0] is a tie

        adj = defaultdict(list) 
        for src, dest in tickets:
            adj[src].append(dest)

        res = ["JFK"]
        # see if we can find a valid path, and update our result accordingly
        def dfs(src):
            if len(res) == len(tickets) + 1: # found our solution! 
                return True  
            if src not in adj:
                return False 

            # modify the adj as we iterate through it to remove the ith index
            # need a temp variable to be able to do this safely 
            temp = list(adj[src])
            for i, v in enumerate(temp): # gives us the index and the neighbor vertex
                adj[src].pop(i)
                res.append(v) 

                if dfs(v): return True

                # backtrack
                adj[src].insert(i, v) 
                res.pop()
            return False 
        
        dfs("JFK")
        return res