class Solution:
    def rob(self, nums: List[int]) -> int:
        

        # decision tree: rob this house or skip it. 
        # if i rob it, and add to the max of two houses ago 
        # if i skip it, i can take the max of the two previous houses...

        two, one = 0, 0 

        for num in nums:
            # rob
            # skip
            cur = max(two + num, one)
            two = one 
            one = cur 

        return one

