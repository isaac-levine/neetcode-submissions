class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # return the amount of cycles (minimum) it takes to complete all tasks 
        taskCounts = Counter(tasks)

        
        # gives us the highest count task at any time (do we even need to know or care what task it is?)
        # at this point, we really just have a bunch of count values that we're concerned with 
        maxHeap = [(-1 * count) for count in taskCounts.values()] # highest count task (* -1) is always at minHeap[0]
        heapq.heapify(maxHeap) # tasks ready to be processed 

        cooldown = deque() # tasks waiting to be processed
        time = 0


        # ["A","A","A","B","C"]

        # {
        # A : 2
        # B : 1
        # C : 1
        # }

    
        while maxHeap or cooldown:
            time += 1

            # if something is ready to be processed right now, process it.
            if maxHeap:
                count = heapq.heappop(maxHeap)
                count += 1 # "decrement"

                if count != 0:
                    cooldown.append((count, time + n)) # can not be processed again until time + n
            
            # check on the waiting room and see if any can graduate to the ready pool 
            if cooldown and time == cooldown[0][1]:
                heapq.heappush(maxHeap, cooldown.popleft()[0])

        
        return time 