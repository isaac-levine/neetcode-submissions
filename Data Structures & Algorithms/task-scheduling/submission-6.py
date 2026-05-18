class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = Counter(tasks)
        maxHeap = [-c for c in counts.values()] # ready to be processed? 
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-count, idleTime], waiting to be processed 

        while q or maxHeap:
            time += 1

            # time optimization: skip to next unprocessed task if that's all we're waiting for 
            if not maxHeap and q:
                time = q[0][1]

            # tasks are ready to be processed
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap) # pop and decerement highest count 
                
                if count < 0: # remember its negative, so <0 means # of tasks is actually > 0
                    q.append([count, time + n]) # this letter (whatever it is) can not be processed again until time + n

            # check if next in queue is ready to be processed again   
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0]) # push this count 


        
        return time