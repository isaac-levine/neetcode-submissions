class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = Counter(tasks) # task -> # of occurences 
        maxHeap = [-c for c in counts.values()] 
        heapq.heapify(maxHeap) # don't forget to heapify it

        q = deque() # pairs of [-count, idleTime]

        time = 0
        while maxHeap or q:

            time += 1

            if maxHeap:
                # pop the most frequently occuring task
                taskCount = 1 + heapq.heappop(maxHeap)
                
                if taskCount < 0:
                    q.append([taskCount, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        
        return time 
        