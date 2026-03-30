# all functions should be done in O(1) time
class MinStack:

    def __init__(self):
        self.mins = []
        self.stack = []

    # pushes the element val onto the stack
    def push(self, val: int) -> None:
        if not self.mins:
            self.mins.append(val)
        else:
            self.mins.append(min(self.mins[-1], val))
        self.stack.append(val)
        
    # removes the element on top of the stack
    def pop(self) -> None:
        self.mins.pop()
        self.stack.pop()
        
    # gets the top element of the stack
    def top(self) -> int:
        return self.stack[-1]
        
    # retreives the minimum element in the stack
    def getMin(self) -> int:
        return self.mins[-1]
        

