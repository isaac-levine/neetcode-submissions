class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # build adjacency list 
        adjList = {src: [] for src, dest in tickets } # from -> to
        for src, dest in tickets:
            adjList[src].append(dest)

        # sort each airtport's destination array
        for airport in adjList:
            adjList[airport].sort() # sort all the destinations from this airport in lex. order

        res = []
        def dfs(adj, result, src): # instead of doing a visit set, you can "modify" the adjList every time 
            if src in adj:
                destinations = adj[src]
                while destinations: 
                    dest = adj[src].pop(0)
                    dfs(adj, res, dest)
                    destinations = adj[src]
            res.append(src)

        dfs(adjList, res, "JFK")
        res.reverse()

        if len(res) != len(tickets) + 1:
            return []

        return res