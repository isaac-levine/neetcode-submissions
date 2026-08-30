class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # binary search over the decision space where decision = where to cut in the bigger one
        total = len(nums1) + len(nums2)
        half = total // 2
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A # make sure A is the smaller of the two arrays
            # we need to do this because if A were bigger, then we could end up with a negative j 
            # by accident 
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # we know countA = i + 1
            j = half - i - 2 # because we know countB = half - countA

            # take care of OOB checks by just using negative infinity as a placeholder val
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            # check if this cut produces the true median we were looking for 
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright) # since we are doing floor division to find A, solution must be on the right??? and we know its one of these 
                else:
                    # even -> halfway between the rightmost of the left and the leftmost of the right
                    leftMax = max(Aleft, Bleft)
                    rightMin = min(Aright, Bright)
                    return (leftMax + rightMin) / 2
            elif Aleft > Bright: # The cut in A is too big, need to move to the left of it
                r = i - 1
            else:
                l = i + 1

