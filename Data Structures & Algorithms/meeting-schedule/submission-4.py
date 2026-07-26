"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True # no overlaps

        # are there any overlaps ? if so, return False. 
        intervals.sort(key = lambda i: i.end) # sort intervals by end time
        prevEnd = intervals[0].end

        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            if start < prevEnd:
                return False
            prevEnd = end
        
        return True