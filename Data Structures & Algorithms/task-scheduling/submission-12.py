class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # i remember this problem for sure we definitely want some sort of cooldown queue 
        # and some sort of heap for which ready task to process first. 
        # i think it's definitely a queue and a maxHeap 

        # every cycle: 
        # - pop off any tasks that are ready from the cooldown queue to the ready heap 
        # - process the highest frequency task from the ready heap 

        # initially, everything should be in the ready heap and nothing should be cooling down yet
        
        time = 0
        taskCounts = Counter(tasks)
        readyHeap = []
        waitingQueue = deque()  # fifo cooldown queue -- (count, readyAtTime)
        for task, count in taskCounts.items():
            heapq.heappush(readyHeap, count * -1) # it doesnt even really matter what letter task it is...

        # X:2 Y:2 n = 2
        # waitingQueue = (1, 4)
        # readyHeap = 
        # time = 4

        while readyHeap or waitingQueue:

            time += 1

            # optimization: fast-forward in time if nothing is ready right now 
            if not readyHeap:
                time = waitingQueue[0][1]

            # 1. pop off any tasks from the waitingQueue that are ready to go on the readyHeap
            while waitingQueue and waitingQueue[0][1] <= time:
                count, _ = waitingQueue.popleft() 
                heapq.heappush(readyHeap, count * -1)

            # 2. process the highest frequency task from the ready heap 
            count = heapq.heappop(readyHeap) * -1
            count -= 1
            if count > 0:
                waitingQueue.append((count, time + n + 1)) # it will be ready at time + n


        
        return time