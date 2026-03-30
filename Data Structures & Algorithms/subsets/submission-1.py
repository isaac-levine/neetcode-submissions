class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # nums are unique integers, don't need to sort and skip 
        curSet, res = [], [] 
        self.backtrack(nums, 0, curSet, res)
        return res
    
    def backtrack(self, nums, i, curSet, res):
        if i >= len(nums):
            res.append(curSet.copy()) # TODO: what does copy() really do?
            return 

        # decision tree: to include nums[i] or not to include 
        curSet.append(nums[i])
        self.backtrack(nums, i + 1, curSet, res)

        curSet.pop()
        self.backtrack(nums, i + 1, curSet, res) 
