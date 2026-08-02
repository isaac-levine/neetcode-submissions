"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # minimum number of rooms. i.e. the maximum number of concurrent meetings at any time -- maximum number of overlapping intervals 

        
        # [(0, 40), (5, 10), (15,20)]
        

        # [(1,5),(2,6),(3,7),(4,8),(5,9)]

        # rooms = [5,]

        if not intervals:
            return 0 

        intervals = sorted(intervals, key = lambda interval : interval.start)
        rooms = [] # minHeap of meeting end times. 
        rooms.append(intervals[0].end)

        for interval in intervals[1:]:
            if interval.start >= rooms[0]:
                heapq.heapreplace(rooms, interval.end)
            else:
                heapq.heappush(rooms, interval.end)


        return len(rooms)