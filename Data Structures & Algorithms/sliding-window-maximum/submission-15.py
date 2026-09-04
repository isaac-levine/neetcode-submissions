class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        res = [] # contains the maximum element for each window k 

        # iirc, i think it helps if you just account for the growing (initial set up to grow to size k window) and the normal process in one loop...

        # need a maxHeap (*-1) with the index to represent the current maximum and be able to get it quickly 

        maxHeap = [] 


        l = r = 0 # i dont love this the way we're starting out with a window that's too small but whatever 
        while r < len(nums):
            
            # pop off old maxes that are no longer in our window 
            while maxHeap and maxHeap[0][1] < l:
                heapq.heappop(maxHeap)
            
            heapq.heappush(maxHeap, ((nums[r] * -1), r)) # add the num at r and its index 
            
            if (r - l + 1) == k:
                res.append(maxHeap[0][0] * -1)
                l += 1
            r += 1 # until window size reaches k, we only move r instead of both ptrs 

        # [1,2,1,0,4,2,6]
        #      l   r
        # maxHeap: (-4, 4), (-1,0), (-1, 2), (0, 3), 
        # res: [2,2,4,]



        return res