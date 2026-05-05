class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        # 1. create the adjacency list representation of the graph
        adjList = {i : [] for i in range(numCourses)}
        for a, b in prerequisites:
            adjList[a].append(b)

        visiting = set()
        def dfs(c):
            if c in visiting:
                return False
            elif adjList[c] == []:
                return True
            else:
                visiting.add(c)
                # process dependencies
                for prereq in adjList[c]:
                    if not dfs(prereq):
                        return False
                visiting.remove(c) # unlock this node
                adjList[c] = [] # mark it as safe for future iterations
                return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True