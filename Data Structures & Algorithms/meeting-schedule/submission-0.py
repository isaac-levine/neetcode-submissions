"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # sort by start time
        intervals.sort(key=lambda i: i.start)

        prevEnd = -1 
        for interval in intervals:
            if interval.start < prevEnd:
                return False
            else:
                prevEnd = interval.end

        return True
