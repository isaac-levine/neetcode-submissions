class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       
        # return true if any value appears more than once in the array, otherwise false

        seen = set() 
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False
