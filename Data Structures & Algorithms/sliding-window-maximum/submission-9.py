class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        res = [] 
        q = deque() 
        l = r = 0

        while r < len(nums):

            # pop from the top/right of the queue if values are smaller. 
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            # pop from the back/left of the queue if that value is no longer in the window 
            if l > q[0]:
                q.popleft()

            # only update res for valid windows, and same for l
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1

        
        return res