"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        time = []

        for i in intervals:
            time.append((i.start, 1)) # on more meeting going on now 
            time.append((i.end, -1)) # one less meeting going on now 

        time.sort()

        count = 0  # number of meetings currently in progress
        maxCount = 0 # the maximum # of meetings in progress at any time
        
        for t in time:
            count += t[1] # add or subtract based on whether this is a start or end time
            maxCount = max(maxCount, count) # re-calculate maxCount

        return maxCount



        
