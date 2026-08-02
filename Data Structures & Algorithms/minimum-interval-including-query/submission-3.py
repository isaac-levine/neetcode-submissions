class Solution:
    #.                       n                          m 
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        

        # query[j] = length of the shortest interval that contains queries[j] (inclusive)

        # return query[] output 

        # so you have your intervals, and just need to return the length of the shortest interval containing the queries[] value 

        intervals.sort() 

        res = {} # q -> interval_length
        minHeap = [] # (interval_length, interval_end), the intervals that contain q. -- so we can grab the shortest whenever we want. 
        i = 0 # global intervals pointer - it only moves forward, because we are sorting intervals

        for q in sorted(queries): # so we don't mutate the original queries array, so we can preserve index order. 

            # add any candidate intervals that contain q  
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, ((r - l + 1), r))
                i += 1

            # pop off any intervals that don't contain q:
            while minHeap and minHeap[0][1] < q: # ends before q
                heapq.heappop(minHeap)
            
            res[q] = minHeap[0][0] if minHeap else -1 # set result for q to the interval_length of the top of the heap. 



        return [res[q] for q in queries]