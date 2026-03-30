class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2 # tells us the total number of elements in the left partition
        
        if len(B) < len(A):
            A, B = B, A # make A the smaller list for simplicity

        # All the work (binary searching) will essentially be done on the smaller of the two arrays

        l, r = 0, len(A) - 1
        while True: # guaranteed to be a median so once we find it we can just return it
            i = (l + r) // 2 # A ptr
            j = half - i - 2 # B ptr -- this is a key insight. also you have to do - 2 because half tells you the number of elements, but i is 0-based index and B indeces also start at 0

            # TODO: why are we doing this?
            # This helps with the comparison and making our life really easy in the next step
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # now our life is easy. we can check:
            # partition is correct --> find the median
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2: # odd number of elements
                    return min(Aright, Bright)
                else: # even
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 # want decimal division
            elif Aleft > Bright: # Aleft is too big, we have too many elements from A --> reduce the size of A
                r = i - 1
            else:
                l = i + 1 # increase the size of our left partition from A
        
        # don't need a return statement outside because we know our loop is eventually going to find a median
        # O(log(min(a, b))) because we're basically running binary search on the smaller (A) of the two lists
        