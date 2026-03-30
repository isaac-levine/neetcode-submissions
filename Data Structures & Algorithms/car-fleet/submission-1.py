class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target = 10, position = [4,1,0,7], speed = [2,2,1,1]
        # cars = [[7,1],[4,2],[1,2],[0,1]]

        n = len(position)
        pos_speed = [[0,0]] * n

        for i in range(n):
            pos_speed[i] = [position[i], speed[i]] 
        
        pos_speed.sort(reverse=True) 

        stack = []
        for p, s in pos_speed:
            # Calculate time to reach the target for the current car
            time = (target - p) / s
            
            # Add the time to the stack
            stack.append(time)
            
            # Check if there are at least two cars in the stack and the current car
            # takes less or equal time than the previous car. If so, pop the previous car.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        # The length of the stack represents the number of car fleets
        return len(stack)
 