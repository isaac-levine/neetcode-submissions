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
        rooms = [] 
        rooms.append(intervals[0])

        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            found_free_room = False

            # check the existing meeting rooms for availability
            for i in range(len(rooms)):
                if start >= rooms[i].end: # this meeting room is now FREE
                    rooms[i] = interval # put this meeting in that room 
                    found_free_room = True
                    break # no longer need to look for a meeting room 
            
            if not found_free_room:
                rooms.append(interval)

        return len(rooms)