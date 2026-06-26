class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        adjList = {i : [] for i in range(numCourses)} 
        for a, b in prerequisites:
            # must take course b first, before taking course a.
            # i.e. a "requires" b. so path must be from b -> a, because b must come first. 
            adjList[b].append(a)

        visited = set() # fully explored. safe. 
        def dfs(course, visiting):
            if course in visiting: # in current path, NOT SAFE. cycle detection
                return False
            if course in visited:
                return True
            
            visiting.add(course)
            for otherCourse in adjList[course]:
                if not dfs(otherCourse, visiting):
                    return False
            visiting.remove(course) # don't forget this part!! 
            visited.add(course)
            return True



        for course in adjList:
            if not dfs(course, set()):
                return False

        return len(visited) == numCourses


        