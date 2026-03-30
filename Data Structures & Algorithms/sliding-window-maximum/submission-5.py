class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        q = collections.deque() # contains indeces instead of values
        l = r = 0

        # Deque = [index_of_biggest_num, ..., ..., index_of_smallest_num]

        while r < len(nums):

            # basically we are adding nums[r] to the window, what needs to happen? 

            # pop all values smaller than nums[r] from the Q
            while q and nums[q[-1]] < nums[r]: 
                q.pop()
            q.append(r)

            # if our max is no longer in the window, remove it from the Q
            if l > q[0]: # left index is further right than index_of_biggest_num
                q.popleft()

            if r >= (k - 1):
                res.append(nums[q[0]]) # and only build the result once we know have a full window, skips the growth phase
                # only incremement left once our window is at least size k
                # so at first only r will be growing, until window reaches size k (i.e. r reaches index k - 1)
                l += 1

            r += 1

        return res