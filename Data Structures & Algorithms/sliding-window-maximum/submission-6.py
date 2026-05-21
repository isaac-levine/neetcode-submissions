class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        res = []
        q = deque() # index -- monotonically decreasing. so top/right is always smallest.

        l = r = 0

        while r < len(nums):
            
            # make sure no smaller values exist in our queue (since this is a monotonically decreasing queue)
            while q and nums[q[-1]] < nums[r]:
                q.pop() # pop from the top of the queue 

            q.append(r)

            # remove left value from the window. 
            if l > q[0]:
                q.popleft()

            # verify that window is at least size k before updating our output 
            # handles the edge case where we do this stuff at the beginning but dont actually update our output
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1

            r += 1
            
        
        return res



