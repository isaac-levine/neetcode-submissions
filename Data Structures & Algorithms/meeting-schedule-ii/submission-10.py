"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0 

        intervals.sort(key = lambda i: i.start)  # do we want to sort by end time? 
        rooms = [] # just holds end times 
        rooms.append(intervals[0].end) # add first end time

        for interval in intervals[1:]:
            if interval.start >= rooms[0]: # the earliest ending room is now FREE (heap[0])
                heapq.heapreplace(rooms, interval.end) # pops the root, pushes the new value, and re-sifts           
            else:
                heapq.heappush(rooms, interval.end) # create a room and add this end time to the heap 

        return len(rooms)