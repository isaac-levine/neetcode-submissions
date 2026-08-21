class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = [] # -3, -3, -2, -1
        for num in nums:
            heapq.heappush(self.minHeap, (num))

    def add(self, val: int) -> int:

        heapq.heappush(self.minHeap, (val))
        print(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]