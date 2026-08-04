class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        a_done, b_done, c_done = False, False, False

        for a, b, c in triplets:
            if a == target[0] and b <= target[1] and c <= target[2]:
                # can never apply this if b or c is > target, because it's irreversible 
                a_done = True
            if b == target[1] and a <= target[0] and c <= target[2]:
                b_done = True
            if c == target[2] and b <= target[1] and a <= target[0]:
                c_done = True

        return a_done and b_done and c_done 
