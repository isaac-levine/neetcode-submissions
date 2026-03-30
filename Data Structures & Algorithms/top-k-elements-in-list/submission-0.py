class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {} 
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        heap = [(-value, key) for key,value in counts.items()]
        kLargest = heapq.nsmallest(k, heap)
        print("kLargest: ", kLargest)
        return [value for key, value in kLargest]
        