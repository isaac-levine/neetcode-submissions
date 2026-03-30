class TimeMap:

    def __init__(self):
        # key1 -> [(time, val), (time, val)] 
        # key2 -> [(time, val), (time, val)]
        
        self.cache = {}

    # Stores the key key with the value value at the given time timestamp.
    # Note: For all calls to set, the timestamps are in strictly increasing order.
    # so we don't have to worry about searching to find where to insert. we can always safely insert to the end 
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []
        self.cache[key].append((timestamp, value))
        

    # Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".
    def get(self, key: str, timestamp: int) -> str:

        timeVals = self.cache.get(key, [])
        res = ""

        l, r = 0, len(timeVals) - 1
        while l <= r:
            mid = (l + r) // 2
            if timeVals[mid][0] == timestamp:
                return timeVals[mid][1]
            elif timeVals[mid][0] > timestamp:
                r = mid - 1 # I'm invalid and so is everything to my right
            else:
                res = timeVals[mid][1] # may overwrite yourself multiple times here
                l = mid + 1 # I am valid and I know everything to my left is worse (even though they are also valid) 

        return res 

