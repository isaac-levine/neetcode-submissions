class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # have h hours to eat all the piles
        # piles[i] = number of bananas in the ith pile 

        # need to find minimum k (bananas per hour rate) such that you still finish all bananas in k hours 
        
        # min: 1 -- if h >= sum(piles), then you can eat 1 banana per hour 
        # max: max(piles) -- you know you're eating a whole pile every single time. so it takes len(piles) hours.
        

        # idea: what if we binary search betweeen 1 and max(piles), trying each possible value k? 

        # if we have a potential solution for k...how do we _verify_ the potential solution?
            # could iterate through the piles and simulate Koko. This would be O(n * log(m)) -- O(n) to simulate and O(log m) to binary search, where m = the maximum value of the array (the biggest pile)  

        # piles = [1,4,3,2], h = 9

        res = max(piles) # 2
        l = 1 # 1 
        r = res # 1
        while l <= r:
            k = (l + r) // 2 # our potential solution for k 
            # check whether this is a valid k
            # too big? --> r = k - 1
            # too small? --> l = k + 1
            # works? --> res = min(res, k)
            
            hoursTaken = 0
            for pile in piles:
                hoursTaken += math.ceil(pile / k) 

            if hoursTaken <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res 

