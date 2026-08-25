class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        taskCount = Counter(tasks)
        q = deque() # deque?                               -- cooling down / waiting room
        maxHeap = [(-1 * c) for c in taskCount.values()] #   -- ready for use 
        heapq.heapify(maxHeap)

        time = 0 
        while maxHeap or q:
            time += 1
            # nothing ready, skip to next time..
            if not maxHeap and q:
                time = q[0][1]

            if maxHeap: 
                count = 1 + heapq.heappop(maxHeap)
                if count < 0: # it's not done yet... needs to go back to the waiting room 
                    q.append((count, time + n))

            # check to see if any are now ready to graduate from waiting room -> maxHeap 
            if q and q[0][1] == time:
                count, availableAt = q.popleft() 
                heapq.heappush(maxHeap, count)

        return time