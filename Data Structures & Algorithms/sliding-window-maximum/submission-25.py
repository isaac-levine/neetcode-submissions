class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # result is maximum element in the window at each step 

        # since we have a fixed-size window of size k we can just a monotonicly decreasing queue? 
        # since we know if there is a big one, we don't need any earlier small ones....if that makes sense. 
        # not sure i'm really internalizing the underlying WHY behind this but I do remember that we want a monotonic queue here 
        # and not a heap. 

        l = 0
        q = deque() # (index) ... in monotonically decreasing order of nums[index]
        res = [] # 2

        # q = 1,2

        #. 0,1,2,3,4,5,6
        # [1,2,1,0,4,2,6], k = 3
        # l.   r

        for r in range(len(nums)): 

            # 1. add nums[r] to the queue after popping anything off the back thats smaller than in it 
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # 2. evict anything from the queue that's no longer in the window (index < l)
            while q and q[0] < l:
                q.popleft()

            # only append result and move l when our window is large enough 
            if (r - l + 1) == k:
                res.append(nums[q[0]]) 
                l += 1
            
        return res 