class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        adjList = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adjList[b].append(a) # b must be taken before a 

        visited = set() 
        def dfs(course, visiting):
            if course in visited:
                return True
            if course in visiting:
                return False
            
            visiting.add(course)
            for otherCourse in adjList[course]:
                if not dfs(otherCourse, visiting):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c, set()):
                return False
        
        return True