class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = list(range(n + 1))

        # union a into b
        def union(a, b):
            par[find(a)] = find(b)

        def find(a):
            while par[a] != a:
                par[a] = par[par[a]]   # point at grandparent — halves depth as you walk
                a = par[a]
            return a


        res = None
        for a, b in edges:
            if find(a) == find(b):
                res = [a,b]
            union(a, b)
        return res