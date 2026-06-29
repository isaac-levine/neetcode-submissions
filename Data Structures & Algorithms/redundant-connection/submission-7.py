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

        allBadEdges = [] 
        for a, b in edges:
            if find(a) == find(b):
                allBadEdges.append([a, b])
            union(a, b)

        return allBadEdges[-1]

            

