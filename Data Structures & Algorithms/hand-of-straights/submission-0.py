class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize:
            return False
        
        # make a count map
        count = {} 
        for h in hand:
            count[h] = count.get(h, 0) + 1

        # sort count by key 
        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            # can we create a group starting at first of size groupSize?
            for i in range(first, first + groupSize):
                if i not in count:
                    return False # not available to us
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        
        return True
