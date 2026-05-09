class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # 0 -> 1
        # 1 -> 2, 3, 4 
        # 2 -> 3
        # 3 -> 
        # 4 -> 

        # visited = 1, 2, 3, 0, 4
        # visiting =
        
        # tree = no cycles and fully connected

        adjList = {i : [] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        visited = set() # check if it's fully connected (if len(visited) = n)
        visiting = set() 

        def dfs(n, parent):
            if n in visiting: 
                return False # found a cycle, this recursive path led back to the same node 
            if n in visited:
                return True # we already know this node is good 
            
            visiting.add(n)

            for neighbor in adjList[n]:
                if neighbor == parent:
                    continue 
                if not dfs(neighbor, n):
                    return False
            
            visiting.remove(n)
            visited.add(n)
            return True
        

        if not dfs(0, None):
            return False
        
        return len(visited) == n
