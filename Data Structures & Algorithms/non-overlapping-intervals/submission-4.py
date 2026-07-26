class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # sort
        # when you detect an overlap, delete the one that reaches further into unknown space (to the right)

        intervals.sort()  # O(N log N)

        # [[1,2],[2,4],[1,4]]
        # res = [[1,2],[2,4],

        res = [] 
        res.append(intervals[0])
        numRemoved = 0 

        for iStart, iEnd in intervals[1:]:
            topStart, topEnd = res[-1][0], res[-1][1]
            
            if iStart < topEnd: # common point does not count as overlapping 
                # overlap --> delete the one that reaches further to the right 
                if topEnd > iEnd:
                    res.pop()
                    res.append([iStart, iEnd])
                numRemoved += 1
            
            
            
            else:
                res.append([iStart, iEnd])

        
        return numRemoved