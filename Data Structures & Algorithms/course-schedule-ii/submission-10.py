class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = {c : [] for c in range(numCourses)}
        for a, b in prerequisites:
            adjList[b].append(a)
        

        visited = set()
        res = []
        def dfs(course, visiting):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)
            for otherCourse in adjList[course]:
                if not dfs(otherCourse, visiting):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True
    
        for c in range(numCourses):
            if not dfs(c, set()):
                return []
        
        return res[::-1]
            

