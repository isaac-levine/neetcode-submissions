class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        

        # union find 
        par = list(range(len(edges) + 1))

        # assign a's parent to b's parent 
        def union(a, b):
            par[find(a)] = find(b) 
        
        # find the parent of a 
        def find(a):
            if par[a] == a:
                return a
            return find(par[a])

        # traverse all edges, keeping track of bad ones because we need to return the LAST bad one.
        allBadEdges = [] 
        for a, b in edges:
            if find(a) == find(b): # if these are ALREADY connected (bad edge), keep track of it
                allBadEdges.append([a, b])
            union(a, b) # union since we know these are connected because we're traversing edges in the first place.

        return allBadEdges[-1]

            

