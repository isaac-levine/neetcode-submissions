class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        par = list(range(n))

        # union x into y
        def union(x, y):
            par[find(x)] = find(y)

        def find(x):
            while par[x] != x:
                return find(par[x])
            return x 

        # kruskal's: add all edges to a minHeap 
        # take the globally cheapest edge if it would connect two distinct components 

        edges = [] 
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        edges.sort()

        numEdgesTaken = 0
        res = 0
        for w, i, j in edges:
            if find(i) != find(j):
                numEdgesTaken += 1
                res += w
                union(i, j)
            
                if numEdgesTaken == n - 1:
                    break
            

        return res 
