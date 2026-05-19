class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        total = len(nums1) + len(nums2)
        half = total // 2
        A, B = nums1, nums2
        # make sure that we are always running binary search on the smaller one 
        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # A
            j = half - i - 2 # index of the midpoint of B. accounting for both off by one errors. 

            # this inline if-elses just help with edge cases making our lives easier
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright: # found the solution
                if total % 2:
                    # odd
                    return min(Aright, Bright)
                else:
                    # even
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright: # # did not find solution, update pointers
                r = i - 1 # A is too big 
            else:
                l = i + 1