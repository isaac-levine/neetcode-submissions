class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        # calculate the time that each car WOULD reach the destination if unblocked 
        # timesToDestination = [] 
        # math.ceil((target - position) / speed)

        # then just go backwards from furthest position to closest, 


        # return the number of groups 
        positionAndSpeed = [[p, s] for p, s in zip(position, speed)]
        stack = [] 

        # going from furthest position out to closest 
        for p, s in sorted(positionAndSpeed)[::-1]: # reverse sorted order 
            timeToEnd = (target - p) / s
            stack.append(timeToEnd)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


        


        return -1 