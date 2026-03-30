class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # count map -> entry items -> k (num), v(count) --> (-count, num) pairs --> heapq.nsmallest(pairs) --> list of vals/nums
        return [v for k, v in heapq.nsmallest(k, [(-value, key) for key,value in Counter(nums).items()])]
        