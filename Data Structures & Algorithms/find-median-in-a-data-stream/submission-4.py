class MedianFinder:

    def __init__(self):
        # small is a maxHeap -- the smaller half, we care about its max
        # large is a minHeap -- the larger half, we care about its min
        self.small, self.large = [], []
        
    def addNum(self, num: int) -> None:
        # just always add it to the small heap
        heapq.heappush(self.small, -1 * num)

        # make sure every num in small is <= every num in large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            heapq.heappush(self.large, (-1 * heapq.heappop(self.small)))

        # make sure sizes are even
        if (len(self.small) > len(self.large) + 1):
            heapq.heappush(self.large, (-1 * heapq.heappop(self.small)))
        if (len(self.large) > len(self.small) + 1):
            heapq.heappush(self.small, (-1 * heapq.heappop(self.large)))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            # even case
            return (-1 * self.small[0] + self.large[0]) / 2.0
        elif len(self.small) > len(self.large):
            return -1 * self.small[0]
        else:
            return self.large[0]


        
        