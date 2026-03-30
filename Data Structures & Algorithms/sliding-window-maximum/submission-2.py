class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        q = deque() # contains indeces in monotic decreasing queue (leftmost is greatest) 
        l = r = 0 

        # max value is always the leftmost value in the deque
        # pop from the rightmost position when we see a new bigger value 
        
        while r < len(nums):
            # make sure no smaller values in q
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)
            
            # remove leftmost in q if it's out of the window
            if l > q[0]:
                q.popleft()
            
            # check that window is atleast size k?
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1 # only move l if window is at least size k

            r += 1
        
        return res

            
