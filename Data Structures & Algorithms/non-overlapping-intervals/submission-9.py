class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # sort
        # when you detect an overlap, delete the one that reaches further into unknown space (to the right)

        intervals.sort(key = lambda interval: interval[1])  # O(N log N)
        res = 0 
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prevEnd:
                res += 1
            else:
                prevEnd = end
        return res