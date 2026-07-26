class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        # for each queries[j], need to find the length of the smallest interval that contains j. 

        intervals.sort() # sort by start time 
        minHeap = [] # (interval_length, end_time) -- kind of represents intervals that could contain q as we are going
        res = {} # q -> answer 
        i = 0 # intervals pointer -- any interval before i we know our q is not in

        for q in sorted(queries): # sort here instead of original because we need to preserve that order for our res

            # check for any intervals that start before q 
            # add these intervals that COULD contain q (based on start time) to our heap and inc. i
            while i < len(intervals) and intervals[i][0] <= q: # interval starts <= q
                l, r = intervals[i]
                heapq.heappush(minHeap, ((r - l + 1), r)) # push (length, end_time)
                i += 1
            
            # pop off any intervals that end before q (expired)
            while minHeap and minHeap[0][1] < q: 
                heapq.heappop(minHeap)
            
            # assign the shortest if there is one else -1 
            res[q] = minHeap[0][0] if minHeap else -1 
            
        return [res[q] for q in queries]