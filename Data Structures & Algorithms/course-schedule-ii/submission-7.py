class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        # starting at every single node, we're going to run DFS from that node
        # output we're trying to build is the order to take courses 

        adjList = {i : [] for i in range(numCourses)} 
        for a, b in prerequisites:
            adjList[a].append(b)

        visited, visiting = set(), set() 
        res = [] 
        def dfs(c):
            if c in visiting: 
                return False # cycle 
            if c in visited:
                return True 
            
            visiting.add(c)

            for prereq in adjList[c]:
                if not dfs(prereq):
                    return False

            visiting.remove(c)
            visited.add(c)
            res.append(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return [] # found cycle
        return res