class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        total = len(nums1) + len(nums2)
        half = total // 2
        A, B = None, None
        if len(nums1) <= len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1
            
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # ptr for A
            j = half - i - 2 # ** - 2 because i is an index of A, and we need to account for the 0-index of B as well.

            # technically any of these could be out of bounds so we can just take care of that now 
            # the j/i would go out of bounds by going too far to the left -- use negative infinity as a placeholder
            # the j+1/i+1 would go out of bounds by going too far to the right -- use positive infinity as a placeholder 
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                # found solution 
                if total % 2:
                    # odd
                    return min(Aright, Bright) # should never both be inf
                else:
                    # even
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


            