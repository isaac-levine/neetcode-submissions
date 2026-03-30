class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort() #  O(n log n)
        minHeap = []
        res = {} # will convert to array later on 
        i = 0
        
        # map each query q to the smallest interval that it belongs to
        for q in sorted(queries): # does the sorting on a copy, not original

            # keep adding intervals until we run out or this interval is too far to the right for this query
            while i < len(intervals) and intervals[i][0] <= q: # make sure query in interval
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            # pop the ones that this interval doesn't belong to (end is too far to the left)
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            # get the smallest interval (index 0)
            res[q] = minHeap[0][0] if minHeap else -1
            

        # convert the res map into an array
        return [res[q] for q in queries]
