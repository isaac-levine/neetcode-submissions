class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        # topological sort. is there a valid topological ordering of this graph? 
        
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)


        visited = set() 
        # top sort is basically just post order dfs with append ? 
        def dfs(course, path):
            if course in visited:
                return True
            if course in path:
                return False
            
            path.add(course)

            for prereq in adj[course]:
                if not dfs(prereq, path):
                    return False
            # path.remove(course)
            visited.add(course)
            return True

        for c in range(numCourses):
            if not dfs(c, set()):
                return False

        return True