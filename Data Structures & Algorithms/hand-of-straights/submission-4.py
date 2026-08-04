class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        n = len(hand)
        if n % groupSize:
            return False
        

        # counts{} card -> count 

        # minHeap tells us what is the smallest card still in play 

        # want to know: can we make even groups of size groupSize s.t. each group contains consecutive hands


        # 1 : 1
        # 2 : 2
        # 3 : 2
        # 4 : 2
        # 5 : 1

        # O(n) time and space
        counts = Counter(hand) # card -> count 

        minHeap = list(counts.keys())
        heapq.heapify(minHeap) # O(n log n) ?? should know this by heart ** 

        while minHeap:
            first = minHeap[0]
            for i in range(first, first + groupSize):
                # try to form this group 
                if i not in counts or counts[i] <= 0:
                    return False
                
                counts[i] -= 1

                if counts[i] == 0:
                    heapq.heappop(minHeap)

        return True
