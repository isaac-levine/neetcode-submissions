class MedianFinder:

    # O(n) space
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        

    # O(log N)
    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, num * -1)
        
        # make sure the two heaps are within size diff of 1 
        if len(self.minHeap) > 1 + len(self.maxHeap):
            heapq.heappush(self.maxHeap, -1 * (heapq.heappop(self.minHeap)))
        elif len(self.maxHeap) > 1 + len(self.minHeap):
            heapq.heappush(self.minHeap, -1 * (heapq.heappop(self.maxHeap)))
        
        
    # O(1) return the head of the bigger heap, else the avg between them if they have equal length  
    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0] * -1
        elif len(self.maxHeap) < len(self.minHeap):
            return self.minHeap[0]
        else:
            return ((self.maxHeap[0] * -1) + (self.minHeap[0])) / 2

        
        