class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        n = len(hand)
        if n % groupSize:
            return False

        numGroups = n // groupSize

        count = Counter(hand)

        # we know n is at least divisible by groupSize now.
        # can we divide into groups of size groupSize where each group is strictly increasing? 


        # [1,2,4,2,3,5,3,4] groupSize = 4 numGroups = 2
        # 1: 1 --> 0 -- popped
        # 2: 2 --> 1 --> 0
        # 3: 2 --> 1 --> 0
        # 4: 2 --> 1 --> 0
        # 5: 1 --> 0

        # we know we're always going to start a group with the smallest available (count > 0) card
        minHeap = [card for card in count.keys()] # allows us to get the smallest available card at any time. 
        heapq.heapify(minHeap)

        for _ in range(numGroups):
            
            # pop off minHeap while count <= 0
            while count[minHeap[0]] <= 0:
                heapq.heappop(minHeap)

            cur = minHeap[0]
            # now that we have the head of the group, see if we can build the whole group 
            for _ in range(groupSize):
                if cur not in count or count[cur] <= 0:
                    return False
                # decremenet it's count and move to the next 
                count[cur] -= 1 
                cur += 1


        return True