class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        # for any point in one array, we know exactly how many we need from the other to test a potential split 
        
        # binary search over one of the arrays (not sure larger or smaller one)

        # nums1: [1,2,*3,4] nums2: [2,5,10]

        #           ^ index 1
    
        # thats a mistake though...we actually want to search over the solution space which is where to make the cut (in the smaller array)
        # so if we search over A where A is the smaller one, and we decide we are going to cut here..
        # then we know we need totalNums // 2 - inThisCut from the B array.

        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        total = len(nums1) + len(nums2)
        half = total // 2
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2

            j = half - i - 2

            # is this even a valid cut?
            Aleft = A[i] if i >= 0 else float("-inf") 
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")

            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2: # odd, so its the first one on the right half. 
                    return min(Aright, Bright) 
                else: # even, so it's the middle between the leftmost and the rightmost 
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
