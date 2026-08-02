class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = [] 

        # intervals is already sorted, and intervals is guaranteed non-overlapping.

        for i in range(len(intervals)):
            start, end = intervals[i]

            if start > newInterval[1]: # starts after newInterval ends, so we know we are done 
                res.append(newInterval)
                return res + intervals[i:]
            elif end < newInterval[0]: # ends before newInterval starts, so just add it to the result and keep looking for a merge conflict 
                res.append([start, end])
            else: # merge conflict: overlaps with newInterval, so merge them together.
                newInterval = [
                    min(start, newInterval[0]),
                    max(end, newInterval[1])
                ]

        # if we got here, we know we never appended newInterval
        res.append(newInterval)
        return res