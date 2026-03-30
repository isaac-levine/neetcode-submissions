class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        res = []
        visit, cycle = set(), set() 
        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            
            cycle.add(c)
            for pre in adjList[c]:
                if not dfs(pre):
                    return False
            cycle.remove(c)
            visit.add(c)
            res.append(c)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return [] 
        return res
        