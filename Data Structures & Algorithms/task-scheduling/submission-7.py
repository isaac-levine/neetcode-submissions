class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        
        counts = Counter(tasks)
        maxHeap = [-c for c in counts.values()] # "ready pool", just counts -- always grab the one with the most remaining work
        heapq.heapify(maxHeap)

        time = 0 
        cooldown = deque() # "waiting room" -- tasks that can not be scheduled right now. (task, available_at_timestamp)



        while maxHeap or cooldown:

            time += 1

            # for each tick of the clock we:
            # 1. pop best candidate from the ready pool -> run it -> then park it in the waiting room if runs remain
            # 2. check waiting room front -> move back to ready pool if its release time is now 

            # 1.
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt += 1 # "decrement" remember we're storing negative values in here 
                if cnt != 0:
                    cooldown.append((cnt, time + n))

            
            # 2. 
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(maxHeap, cooldown.popleft()[0])

        return time