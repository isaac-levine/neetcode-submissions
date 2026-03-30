class MinStack:

    def __init__(self):
       self.mins = [] # keeps track of min at time i 
       self.values = []

    def push(self, val: int) -> None:
        self.values.append(val)
        val = min(val, self.mins[-1] if self.mins else val)
        self.mins.append(val)

    def pop(self) -> None:
        self.values.pop()
        self.mins.pop()

    def top(self) -> int:
       return self.values[-1] 

    def getMin(self) -> int:
        return self.mins[-1]
        

