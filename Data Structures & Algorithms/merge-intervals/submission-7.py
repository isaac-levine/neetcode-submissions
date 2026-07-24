class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # merge the intervals by star ttime 
        # build res
        # always check for overlap before adding, othewrwise overwrite res[-1]

        # O(n log n)
        intervals.sort() # how do you sort based on start time? 

        # O(n) to build res 
        res = [] 
        for start, end in intervals:
            
            # 1. res is empty (only happens once)
            if not res:
                res.append([start, end])
            
            # 2. tail overlaps with [start, end]
            if start <= res[-1][1]:
                res[-1][0] = min(res[-1][0], start)
                res[-1][1] = max(res[-1][1], end)
            else: # 3. tail does not overlap
                res.append([start, end])

        return res