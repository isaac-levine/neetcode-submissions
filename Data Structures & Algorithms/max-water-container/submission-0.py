class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            min_height = min(heights[l], heights[r])
            width = r - l
            volume = min_height * width

            # update res if volume is bigger
            res = max(res, volume)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return res


# s = Solution()
# print(s.maxArea([2,2,2]), "should be 4")
# print(s.maxArea([1,7,2,5,4,7,3,6]), "should be 36")

