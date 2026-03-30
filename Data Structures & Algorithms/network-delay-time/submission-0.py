class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # build adj list
        adj = {i : [] for i in range(1, n + 1)}
        for s, d, t in times:
            adj[s].append((d, t)) # edge from s to d costs time t.
        
        shortest = {}
        minHeap = [(0, k)] # time from k and destination 
        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = t1
            
            # dest. node and time for each neighbor
            for n2, t2 in adj[n1]:
                if n2 not in shortest:
                    # need to remember to pusht the sum of the weights/times here
                    heapq.heappush(minHeap, (t1 + t2, n2))
        
        if len(shortest) != n:
            return -1
        
        maxTime = 0
        for node, time in shortest.items():
            maxTime = max(time, maxTime)

        return maxTime