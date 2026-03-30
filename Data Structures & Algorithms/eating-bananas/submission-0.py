class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we have n piles of bananas
        # we have to eat all the bananas within h hours

        # deteremine the minimum bananas per hour (k) that she should eat  
        # can only eat at most one entire pile of bananas in a given hour
        # so h >= len(piles) guaranteed
        
        # brute force -> start at 1, check if it works, and then increase if it doesn't 
        # better -> binary search through the solution space 

        # best k = 1, worse k = max(piles) 
        
        l, r = 1, max(piles) 
        res = r

        while l <= r:
            k = (l + r) // 2
            # try this k value
            hoursRequired = 0 
            for p in piles:
                hoursRequired += math.ceil(p / k)
            works = hoursRequired <= h 

            if works:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
            
        return res
