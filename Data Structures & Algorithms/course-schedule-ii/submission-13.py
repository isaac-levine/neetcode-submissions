class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        # return a valid topological ordering 

        adj = defaultdict(list)
        # must take course b before taking a, a -> (requires) -> b
        for a, b in prerequisites:
            adj[a].append(b)

        # 1->0, 3


        # topological sort: explore all neighbors fully and then append this one? 
        res = [] 
        visited = set()
        def dfs(node, path):

            if node in path:
                return False
            if node in visited:
                return True

            path.add(node)
            for nei in adj[node]:
                if not dfs(nei, path):
                    return False

            path.remove(node)
            res.append(node)
            visited.add(node)
            return True
                

        for i in range(numCourses):
            if not dfs(i, set()):
                return []
        return res 