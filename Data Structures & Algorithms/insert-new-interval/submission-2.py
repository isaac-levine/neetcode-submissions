class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        
        res = [] 

        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]: # ends before newInterval starts -> add it
                res.append(intervals[i])
            elif intervals[i][0] > newInterval[1]: # starts after newInteral ends -> add newInterval, then rest b/c we're done (sorted order)
                return res + [newInterval] + intervals[i:]
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res