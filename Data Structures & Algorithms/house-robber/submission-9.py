class Solution:
    def rob(self, nums: List[int]) -> int:

        # if len(nums) == 1:
        #     return nums[0]
        # elif len(nums) == 2:
        #     return max(nums[0], nums[1])

        # profit = [0] * len(nums)
        # profit[0], profit[1] = nums[0], max(nums[1], nums[0])

        # for i in range(2, len(nums)):
        #     profit[i] = max(profit[i - 2] + nums[i], profit[i - 1]) # can take close or far + nums[i]
        
        # return profit[len(nums) - 1]

            
        
        far, close = 0, 0

        for num in nums:
            cur = max(far + num, close)
            far = close
            close = cur 

        return close 
