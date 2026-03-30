class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # return a two sum pair indeces (1-indexed) s.t. i1 < i2 

        # numbers = [1,2,3,4], target = 3
        #            l r 

        # idea: take the first and the last at first. 
        # overshoot -> move the right
        # undershoot -> move the left


        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            elif total > target:
                r -= 1
            elif total < target:
                l += 1
        




