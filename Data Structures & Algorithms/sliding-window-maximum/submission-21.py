class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        # maximum element in each size-k window throughout the array
        # off bat: i think monotonic queue? that stores the windowMax? 
        # so we will drain the queue so long as what we are adding is bigger

        # the reason this is a monQ and not a maxHeap is because our pop and append 
        # pattern is very predictable? and we are not 

        # [1,2,1,0,4,2,6]    k = 3
        # l.   r

        # q = 2

        q = deque()  # (num, index)
        res = [] 

        l = 0 
        for r in range(len(nums)):

            # pop any from the left that are now out of bounds 

            while q and nums[q[-1]] < nums[r]: # pop any from the right that are smaller than what we're about to add
                q.pop() 

            q.append(r)

            if l > q[0]:
                q.popleft()

            # incremement l and update res if we have grown to size k
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            
                

        return res
