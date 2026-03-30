
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        pre, post, res = [0] * n, [0] * n, [0] * n
        pre[0] = nums[0]
        post[n - 1] = nums[n - 1]
        
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i]

        for i in range(n - 2, -1, -1):
            post[i] = post[i + 1] * nums[i]

        res[0] = post[1]
        res[n - 1] = pre[n - 2]

        for i in range(1, n - 1):
            res[i] = pre[i - 1] * post[i + 1]

        return res
