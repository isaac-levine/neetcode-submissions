class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = {i : [] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        visited = set()
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for neighbor in adjList[i]:
                dfs(neighbor)                
        

        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res
