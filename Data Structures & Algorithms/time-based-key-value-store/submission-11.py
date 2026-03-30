class TimeMap:

    def __init__(self):
        self.map = {} # key -> [(time, val), (time, val) ...] 

    # Stores the key with val value at the given timestamp
    # Note: all set call timestamps are in strictly increasing order
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value)) 

    # Returns the most recent value of key if
        # set was already called on it 
        # AND the most recent timestamp for that key is <= the given timestamp
    # if there are no values, returns ""
    def get(self, key: str, timestamp: int) -> str:
        # get the list for this key
        timeVals = self.map.get(key, [])

        # binary search on it and return the most recent timestamp for which that key is <= our timestamp
        l, r = 0, len(timeVals) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if timeVals[mid][0] == timestamp:
                return timeVals[mid][1]
            elif timeVals[mid][0] < timestamp:
                res = timeVals[mid][1]
                l = mid + 1
            elif timeVals[mid][0] > timestamp:
                r = mid - 1

        return res 

