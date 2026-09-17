class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque()  # (num, index)
        res = [] 

        l = 0 
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]: # pop any from the right that are smaller than what we're about to add
                q.pop() 

            q.append(r)

            if l > q[0]:
                q.popleft() # pop from left if its no longer in our window 

            if (r - l + 1) >= k: # move l and update res if we have grown to size k
                res.append(nums[q[0]])
                l += 1                

        return res
