class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # convert edges to adjList
        adjList = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        # dfs --> # of nodes in this CC 
        visited, visiting = set(), set()
        def dfs(n):
            if n in visited or n in visiting:
                return 0 
            elif adjList[n] == []:
                return 1
            
            visiting.add(n)
            numNodes = 1
            for nei in adjList[n]:
                numNodes += dfs(nei)
            visiting.remove(n)
            visited.add(n)
            return numNodes
        
        res = 0
        for i in range(n):
            if dfs(i) > 0:
                res += 1
        return res

            
