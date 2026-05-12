class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # iterate through the edges
            # if a, b are already connected (same parent), then add this edge to the list of duplicate edges. 
            # union the two nodes. 

        # return the last edge in the list of duplicate edges. 

        N = len(edges)
        par = [i for i in range(N + 1)]
        def union(a, b):
            par[find(b)] = find(a)

        def find(a): 
            if par[a] != a:
                return find(par[a])
            else:
                return a

        badEdges = [] 
        for a, b in edges:
            if find(a) == find(b):
                badEdges.append([a, b])
            union(a, b)
        
        return badEdges[len(badEdges) - 1]