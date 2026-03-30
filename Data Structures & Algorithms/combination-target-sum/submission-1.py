class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # the same number may be chosen from nums an unlimited number of times
        # frequency of numbers defines whether two combinations are the same 

        # sort nums O(N Log N) 

        # nums = [2,5,6,9]
        # target = 9


        #               /         \  
        #              2    
        #       /    \        / \  
        #       2,5      2      5  
        #      /  \     / \ 
        # 2,5,6   2,5  2,6 2 


        res = [] 

        def backtrack(i, cur, total):
            if total == target:
                res.append(cur[:]) # since we're going to continue to use this variable across different recursive calls
                return # success base case 
            if i >= len(nums) or total > target:
                return # fail base case

            # choose to include this number
            cur.append(nums[i])
            backtrack(i, cur, total + nums[i])
            cur.pop()
            # make sure we skip duplicates because this is the No branch of the decision tree
            while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1, cur, total) 


        backtrack(0, [], 0) 
        return res

