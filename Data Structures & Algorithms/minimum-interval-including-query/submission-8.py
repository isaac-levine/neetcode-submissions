class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        # return [] of length of shortest interval i such that the interval contains i, inclusive. 
        # if no such interval exists, it will be -1 in the array

        shortest = {} # query -> length of shortest interval that includes 
        intervals.sort() 
        minHeap = [] # (length, index)
        i = 0 

        for q in sorted(queries):
            # add any intervals that start before q to the minHeap by length
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(minHeap, (intervals[i][1] - intervals[i][0] + 1, i))
                i += 1

            # pop off any intervals that end before q
            while minHeap and intervals[minHeap[0][1]][1] < q:
                heapq.heappop(minHeap)
            
            if minHeap:
                shortest[q] = minHeap[0][0] # shortest length 
            else:
                shortest[q] = -1

        
        res = [] 
        for q in queries:
            res.append(shortest[q])
        return res