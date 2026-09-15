class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A # keep A smaller. 

        total = len(A) + len(B)
        half = total // 2

        # binary search over the cut size...where cut = how many elements to take from smaller array
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # A pointer
            j = half - i - 2 # B pointer

            Aleft = A[i] if i >= 0 else float("-inf") # edge of left half of A
            Aright = A[i + 1] if i < len(A) - 1 else float("inf") # edge of right half of A

            Bleft = B[j] if j >= 0 else float("-inf") # edge of left half of B
            Bright = B[j + 1] if j < len(B) -1 else float("inf") # edge of right half of B

            # is this even a valid cut? 
            if Aleft <= Bright and Bleft <= Bright:
                # valid cut...now is it a median???
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                # too much of A, need to go left
                r = i - 1
            else:
                l = i + 1



