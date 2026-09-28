class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # off bat I remember we need a cooldown queue and a ready heap. 
        taskCounts = Counter(tasks)
        q = deque() # cooldown queue -- (readyAtTime, numTasks)
        maxHeap = [] # ready maxHeap -- (-numTasks)

        for numTasks in taskCounts.values():
            heapq.heappush(maxHeap, (-1 * numTasks))

        time = 0 

        # time = 4
        # maxHeap = 1
        #     q   = (4, -1)

        while q or maxHeap:
            time += 1
            if q and not maxHeap:
                time = q[0][0] # optimization, fast forward when there's no work to do. 
            
            # move anything thats done cooling down to the ready maxHeap
            # if its time is <= current time. 
            while q and q[0][0] <= time:
                _, numTasks = q.popleft() 
                heapq.heappush(maxHeap, numTasks)

            # process the top task off of the maxHeap (ready heap) 
            if maxHeap:
                taskCount = heapq.heappop(maxHeap) + 1
                if taskCount < 0:
                    q.append((time + n + 1, taskCount)) # time + n + 1 is the first tick that this may legally graduate from the cooldown queue again...
        
        return time