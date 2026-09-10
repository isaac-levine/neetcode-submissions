class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        # find query[] where query[j] = the length of the shortest interval such that queries[j] is in that interval[i] (inclusive)
        # else -1 if no such interval exists 

        shortest = {}  # query -> shortestIntervalLength

        intervals.sort() # sort intervals by left bound  -- but what does sorting this even get me? 

        minHeap = []  # (-length, intervalIndex)
        # no wait we cant prefill this minHeap we need to maintain it as we go and we need an i pointer to make sure we don't add an interval before we reach its left bound with a q
        # for i in range(len(intervals)):
        #     l, r = intervals[i]
        #     heapq.heappush(minHeap, ((r - l + 1), i))

        # we're going in sorted query order so we know that once we see an interval that is left of this query, we're never going to be able to use 
        # that interval so we might as well pop it off and get rid of it....
        i = 0

        for q in sorted(queries): # I remember that we wanna keep the original queries array unmodified so we can use queries[] to build our result structure 

            # add any intervals to the minHeap that are now reachable by q
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, ((r - l + 1), i))
                i += 1
            
            # pop off any intervals from the minHeap who's right is left of q. -- we know any future q's are right of this q so those intervals are now useless....
            while minHeap and intervals[minHeap[0][1]][1] < q:
                heapq.heappop(minHeap)
            
            # now we now the biggest one containing q is at the head
            shortest[q] = (minHeap[0][0]) if minHeap else -1 


        return [shortest[q] for q in queries]