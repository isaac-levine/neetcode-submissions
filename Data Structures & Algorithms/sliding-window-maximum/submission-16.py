class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        res = [] # contains the maximum element for each window k 

        # iirc, i think it helps if you just account for the growing (initial set up to grow to size k window) and the normal process in one loop...

        # need a maxHeap (*-1) with the index to represent the current maximum and be able to get it quickly 

        q = deque() # only needs to store indeces 

        l = r = 0 # i dont love this the way we're starting out with a window that's too small but whatever 
        while r < len(nums):
            
            while q and nums[q[-1]] < nums[r]: # pop off any values in the queue that are smaller than r...
            # because we know that now that r is in the queue, it will be in here for longer than those values 
                q.pop() # and this allows us to maintain monotonically decreasing order....nothing smaller than
                # nums[r] sits to its left in the queue 
            
            q.append(r) # remember just append the index

            if q[0] < l:
                q.popleft()
            
            if (r - l + 1) == k:
                # only append to res when we know our window has reached size k.
                # same with moving l
                res.append(nums[q[0]])
                l += 1
            r += 1 # until window size reaches k, we only move r instead of both ptrs 



        return res