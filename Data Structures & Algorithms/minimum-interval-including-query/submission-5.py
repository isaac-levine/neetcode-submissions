class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        

        # need to build query[]
        # query[j] = length of shortest interval in intervals[] such that queries[j] is contained inside it (inclusive)

        # for each queries, length of shortest interval in intervals that contains the query 

        intervals.sort() # sorted by start time 
        minHeap = [] # (length, end) efficiently gives us the minimum size interval for our current query 
        res = {} # q -> length 
        i = 0
 
        for q in sorted(queries):

            # add any intervals that could contain this query (compare q to start time)
            while i < len(intervals) and intervals[i][0] <= q:
                l = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(minHeap, (l, intervals[i][1]))
                i += 1

            # remove any intervals that do not contain this query (compare q to end time)
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            res[q] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]