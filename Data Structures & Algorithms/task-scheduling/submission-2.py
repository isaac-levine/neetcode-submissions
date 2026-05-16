class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        

        count = Counter(tasks) 
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap) # maxHeap of counts


        time = 0 
        q = deque() # pairs of [-cnt, idleTime]

        # always process the highest count task
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1] # fast forward in time to whatever the top of the q needs
            else:
                cnt = 1 + heapq.heappop(maxHeap) # remember our counts are negative, so we add one
                if cnt < 0:
                    q.append([cnt, time + n]) # this one can not be processed until time + n
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0]) # if it's time, pop this off the queue and add it to maxHeap
                
        return time