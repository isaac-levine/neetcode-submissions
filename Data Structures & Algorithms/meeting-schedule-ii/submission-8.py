"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # find the minimum number of rooms required to scheudle all the meetings
        # overlap -> + 1 room

        # things we know how to do: merge & drop conflicts (from prior intervals problems)

        if not intervals:
            return 0 


        
        intervals.sort(key = lambda i: i.start)  # do we want to sort by end time? 
        rooms = [] # just holds end times 
        rooms.append(intervals[0].end) # add first end time

        for interval in intervals[1:]:

            # check the existing meeting rooms for availability

            if interval.start >= rooms[0]: # the earliest ending room is now FREE (heap[0])
                heapq.heapreplace(rooms, interval.end) # pop and replace             
            else:
                heapq.heappush(rooms, interval.end) # create a room and add this end time to the heap 

        return len(rooms)