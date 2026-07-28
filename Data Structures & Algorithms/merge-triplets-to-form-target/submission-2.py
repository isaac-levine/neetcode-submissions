class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        a_good, b_good, c_good = False, False, False

        for a, b, c in triplets:
            if (a == target[0] and b <= target[1] and c <= target[2]):
                a_good = True
            if (b == target[1] and a <= target[0] and c <= target[2]):
                b_good = True
            if (c == target[2] and a <= target[0] and b <= target[1]):
                c_good = True
        
        return a_good and b_good and c_good