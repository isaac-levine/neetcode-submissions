class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize:
            return False
        
        count = Counter(hand)
        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            # can we create a group starting at first of size groupSize?
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1 # decrement this i 

                # if you just ran out of some value, but its not the minimum, then there must be a gap -> return False.
                # but if you ran out of some value and its not the minimum, thats just pop it.    
                if count[i] == 0:
                    if i != minH[0]:
                        return False # 
                    heapq.heappop(minH)
        
        return True
