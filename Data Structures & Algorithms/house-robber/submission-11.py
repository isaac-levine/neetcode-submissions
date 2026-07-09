class Solution:
    def rob(self, nums: List[int]) -> int:
        

        # one question to ask at every house you see. rob it or skip it ?
        # and your two variables are:
        #  1. best loot if you decide to rob house [i-2] (Far)
        #  2. best loot if you decide to rob house [i-1] (Close)

        close, far = 0, 0 

        for num in nums:
            cur = max(close, far + num)
            far = max(close, far) 
            close = cur 

        return close