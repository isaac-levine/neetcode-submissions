class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        


        q = deque() # monotonically decreasing --> 
                    # top/right of the q is the smallest 
                    # back/left of the q is the biggest.
        res = []
        l = 0

        for r in range(len(nums)):

            while q and nums[q[-1]] < nums[r]:
                q.pop() # pop from the top of the queue until top of the queue is smaller than nums[r]

            q.append(r)

            # check if we need to pop out the left 
            if q[0] < l:
                q.popleft() 

            # only add to res once window is right size
            if r >= k - 1:
                res.append(nums[q[0]])
                l += 1
            
            r += 1

        return res