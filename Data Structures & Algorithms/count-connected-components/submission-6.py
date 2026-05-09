class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = {i : [] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        print(adjList)
        
        # 0 -> 1, 2
        # 1 -> 0, 2
        # 2 -> 0, 1

        # 3 -> 4
        # 4 -> 3 


        numConnectedComponents = 0 

        visited = set() 
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for neighbor in adjList[node]:
                dfs(neighbor)
                   

        for i in range(n):
            if i not in visited:
                dfs(i)
                numConnectedComponents += 1
        
        return numConnectedComponents
            