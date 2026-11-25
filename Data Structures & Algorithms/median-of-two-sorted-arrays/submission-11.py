class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # if we just binary search one of the arrays, then do we know where we need to be in the other one? 
        # binary search the smaller one -- because it will be faster
        # oh wait no, you binary search the solution space..because that's something we can do
        # wait but if the solution space is where to cut then the one we binary search over 
        # needs to be the bigger array (A)
        # so if the solution space is where to cut one of the arrays..lets say the smaller one 

        # make A smaller so we know our cut will always land in B
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        total_len = len(A) + len(B)
        half = total_len // 2

        # A = [1, 2]
        # B = [3]

        l, r = 0, len(A)
        while l <= r:
            i = (l + r ) // 2 # i = how many elements A gives away.
            # remember, count convention is to point at gaps between elements, not elements themselves.
            # A =      1     3     8
            #        ^     ^     ^     ^
            # gap:   0     1     2     3
            j = half - i

            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")
            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")

            # is this a attempt a valid cut?
            if Aleft <= Bright and Bleft <= Aright:
                # valid cut.
                if total_len % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                # too much from A, go left
                r = i - 1
            else:
                # go right
                l = i + 1