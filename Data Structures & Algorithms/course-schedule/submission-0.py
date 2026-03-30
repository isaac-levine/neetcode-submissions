class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adjList from list of edges
        adjList = {i:[] for i in range(numCourses)} 
        for src, dest in prerequisites:
            adjList[src].append(dest)
        
        # dfs -- is this course completable
        visiting = set() 
        def dfs(c):
            if c in visiting:
                return False
            if adjList[c] == []: 
                return True
            
            # visit this node
            visiting.add(c)
            for prereq in adjList[c]:
                if not dfs(prereq):
                    return False
            visiting.remove(c) # done visiting it 
            adjList[c] = [] # completable
            return True



        # are all courses completable?
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
