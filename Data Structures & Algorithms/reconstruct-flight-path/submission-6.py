class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # Without even reading the problem I think I might remember this being an Eulerian path
        # reconstruct the path assuming each edge (ticket) used exactly once -- can revisit nodes 

        # return lexicographically smallest path -- just sort tickets first? 

        # so what is the algorithm for finding an eulerian path?
        # iirc its just like post order dfs? and then you reverse at the end or something like that
        # explore all neighbors then append myself
        # wait but you can revisit nodes, so cant use a normal visited set and dfs on nodes.....
         
        tickets.sort(reverse=True) 
        path = [] 

        adj = defaultdict(list)
        for src, dest in tickets:
            adj[src].append(dest)

        def dfs(node):
            while adj[node]:
                dfs(adj[node].pop())
            path.append(node)

        dfs("JFK")
        return path[::-1]

