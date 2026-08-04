class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize:
            return False

        counts = Counter(hand) # card -> count 

        minHeap = list(counts.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]
            # try to form the group starting at first.
            for i in range(first, first + groupSize):
                if i not in counts or counts[i] <= 0:
                    return False 
                counts[i] -= 1 
                if counts[i] == 0:
                    heapq.heappop(minHeap)

        return True
