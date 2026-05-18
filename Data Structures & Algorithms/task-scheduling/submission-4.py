class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = Counter(tasks)
        maxHeap = [-c for c in counts.values()] # ready to be processed? 
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-count, idleTime], waiting to be processed 

        while q or maxHeap:
            time += 1

            if maxHeap:
                count = 1 + heapq.heappop(maxHeap) # pop and decerement highest count 
                
                if count < 0: # remember its negative, so <0 means # of tasks is actually > 0
                    q.append([count, time + n]) # this letter (whatever it is) can not be processed again until time + n
                
            if q and q[0][1] == time: # time for this unprocessed one to be processed again 
                heapq.heappush(maxHeap, q.popleft()[0]) # push this count 

            # if not maxHeap and q:
            #     time = q[0][1]
        
        return time