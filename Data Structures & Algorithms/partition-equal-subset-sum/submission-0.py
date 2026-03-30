class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2: # impossible for odd lengths
            return False
        
        target = sum(nums) // 2
        dp = set() 
        dp.add(0)

        for num in nums:
            toAdd = set()
            for subTotal in dp:
                if num + subTotal == target:
                    return True
                elif num + subTotal not in dp:
                    toAdd.add(num + subTotal)
            for x in toAdd:
                dp.add(x)

        return False

