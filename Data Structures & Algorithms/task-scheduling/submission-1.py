class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # O(n * m) where n is # of tasks and m is idle time 
        
        counts = Counter(tasks) # hashmap of each task : count 

        maxHeap = [-count for count in counts.values()] # since heapify is a minHeap, no native maxHeap in py
        heapq.heapify(maxHeap) # order by most negative (our max)
        
        time = 0
        q = deque() # pairs of [-count, idleTime]

        while maxHeap or q:
            time += 1

            if (maxHeap):
                count = 1 + heapq.heappop(maxHeap) # add since we're using negative values 
                if count:
                    q.append([count, time + n]) # current time + n is when it will be available again
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])


        return time