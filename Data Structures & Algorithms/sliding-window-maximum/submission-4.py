class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        q = collections.deque() # contains indeces instead of values
        l = r = 0

        while r < len(nums):
            # pop smaller values from the Q
            while q and nums[q[-1]] < nums[r]: 
                q.pop()
            q.append(r)

            # if our max was the one we're leaving behind, pop it 
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                res.append(nums[q[0]])
                # only incremement left once our window is at least size k
                l += 1

            
            r += 1

        return res