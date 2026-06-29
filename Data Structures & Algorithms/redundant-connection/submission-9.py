class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # basic union find setup -- this should be second nature
        par = list(range(len(edges) + 1))

        def find(a):
            if par[a] == a:
                return a # found it 
            return find(par[a]) # keep looking 

        def union(a, b): # assign a's parent to b's 
            par[find(a)] = find(b)

        
        allBadEdges = [] 
        for a, b in edges:
            if find(a) == find(b):
                allBadEdges.append([a, b])
            union(a, b)
        return allBadEdges[-1]

