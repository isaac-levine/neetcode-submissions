class Solution:
    def climbStairs(self, n: int) -> int:
        

        # return number of distinct ways to climb to stair n
        # you can climb 1 or 2 steps at a time 

        
        # 1 --> 1 --> 1
        # 2 --> 1,2  | 2 --> 2
        # 3 --> 1, 2, 3 | 1, 3 | 2, 3 --> 3
        # 4 --> 1,2,3,4 | 1,3,4 | 2,3,4 | 2,4 | 1,2,4 --> 5


        # intuition: there's x ways to get to n - 2 and y ways to get to n - 1.  but from n - 2 to n there's only 1 way without touching n -1, and from n - 1 to n there's only 1 way
        # so there's always memo[n - 2] + memo[n - 1] ways to get to n 


        two = 1 # ways to reach 0 
        one = 1 # ways to reach 1
        
        for i in range(n):
            tmp = one       # save current "one behind"
            one = one + two # new "one behind" becomes sum of previous two steps 
            two = tmp       # "two behind" becomes previous "one behind"

        return two