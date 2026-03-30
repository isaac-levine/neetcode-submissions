class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)
        heap = [(-value, key) for key,value in counts.items()]
        kLargest = heapq.nsmallest(k, heap)
        return [value for key, value in kLargest]
        