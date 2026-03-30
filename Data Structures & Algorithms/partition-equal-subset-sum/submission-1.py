class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2: # impossible for odd lengths
            return False
        
        target = sum(nums) // 2
        dp = set() 
        dp.add(0)

        for num in nums:
            updatedDP = set()
            for subTotal in dp:
                if num + subTotal == target:
                    return True
                updatedDP.add(num + subTotal)
                updatedDP.add(subTotal)
            dp = updatedDP

        return False

