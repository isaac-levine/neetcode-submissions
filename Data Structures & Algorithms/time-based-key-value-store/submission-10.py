class TimeMap:

    def __init__(self):
        self.keyMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyMap:
            self.keyMap[key] = []
        self.keyMap[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.keyMap:
            # binary search based on timestamps to find which key to return
            pairs = self.keyMap.get(key)
            l, r = 0, len(pairs) - 1
            while l <= r:
                mid = (l + r) // 2
                if pairs[mid][1] <= timestamp:
                    res = pairs[mid][0]
                    l = mid + 1
                else:
                    r = mid - 1
        return res
