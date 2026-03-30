class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort() # is the lambda necessary?
        res = []
        res.append(intervals.pop(0))

        while len(intervals) > 0:
            popped = intervals.pop(0)
            overlap = (popped[0] >= res[-1][0] and popped[0] <= res[-1][1])
            if overlap:
                res[-1] = [min(popped[0], res[-1][0]), max(popped[1], res[-1][1])]
            else:
                res.append(popped)
        
        return res