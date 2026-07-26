class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # sort
        # when you detect an overlap, delete the one that reaches further into unknown space (to the right)

        intervals.sort()  # O(N log N)


        res = 0 
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd: # no overlap
                prevEnd = end
            else: # overlap
                res += 1
                prevEnd = min(prevEnd, end) # remove the one that reaches further to the right

        return res