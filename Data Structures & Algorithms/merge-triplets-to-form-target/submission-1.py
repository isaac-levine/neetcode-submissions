class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        numGoodA, numGoodB, numGoodC = 0, 0, 0

        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            
            if a == target[0]:
                numGoodA += 1
            
            if b == target[1]:
                numGoodB += 1

            if c == target[2]:
                numGoodC += 1
        
        return numGoodA > 0 and numGoodB > 0 and numGoodC > 0