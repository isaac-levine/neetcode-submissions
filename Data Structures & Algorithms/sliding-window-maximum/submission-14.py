class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # sliding window with a minHeap and a count

        # the one we are losing to the left gets count -= 1
        # if the one we are losing to the left is the head and count == 0, pop it off the heap 

        res = []
        q = deque() 
        l, r = 0, 0 

        while r < len(nums):

            # step 1: pop anything from the back that would be dominated by addition of r
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r) # step 2: add r

            # step 3: pop anything from the front thats no longer in the window
            if l > q[0]:
                q.popleft() 

            # step 4: update stuff -- allow r to grow freely if we haven't reached size k yet.
            if r >= k - 1: # r must at least reach index k - 1 before we can start updating l and res
                res.append(nums[q[0]])
                l += 1
            r += 1
        
        return res


            