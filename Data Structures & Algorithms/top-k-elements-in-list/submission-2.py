class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # heap = [(-value, key) for key,value in Counter(nums).items()]
        # kLargest = heapq.nsmallest(k, heap)
        # return [value for key, value in kLargest]

        return [v for k, v in heapq.nsmallest(k, [(-value, key) for key,value in Counter(nums).items()])]
        