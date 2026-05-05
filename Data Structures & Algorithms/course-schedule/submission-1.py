class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # 1. create the graph (adjacency list)
        adjList = {i:[] for i in range(numCourses)}
        for a, b in prerequisites: 
            adjList[a].append(b) # a depends on b

        visiting = set() 
        # 2. dfs --> is this course completable or not? 
        def dfs(c):
            if c in visiting:
                return False # not completable, found a loop.
            if adjList[c] == []:
                return True # completable, no dependencies. 
            
            visiting.add(c)
            for prereq in adjList[c]:
                if not dfs(prereq):
                    return False
            visiting.remove(c)
            adjList[c] = [] # mark it as always safe. 
            return True

        # 3. launch the dfs from each course 
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True