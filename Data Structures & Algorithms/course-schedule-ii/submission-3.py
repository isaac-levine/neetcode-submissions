class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        # build the adjacency list representation of the graph
        adjList = {i : [] for i in range(numCourses)}
        for a, b in prerequisites:
            adjList[a].append(b)

        # a course has 3 possible states:
        # visited -> course has been added to the output already
        # visiting -> course has not been added to the output, but is in the current cycle 
        # unvisited -> course has not yet been added to the output or cycle
        visited, visiting = set(), set() 
        output = [] 
        def dfs(c):
            if c in visiting:
                return False # cycle detected
            if c in visited:
                return True # don't need to visit it twice 
            
            visiting.add(c) # add this course to the current cycle 
            
            for prereq in adjList[c]:
                if not dfs(prereq):
                    return False # we detected a cycle 

            visiting.remove(c) # no longer in the cycle 
            visited.add(c) # now its fully visited
            output.append(c) # add it to the output 
            return True

        for c in range(numCourses):
            if not dfs(c):
                return [] # if any call detects a cycle then we have to return an empty list
        
        return output

        
                