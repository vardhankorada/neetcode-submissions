"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        store = {}
        for interval in intervals:
            st,en = interval.start,interval.end
            if st in store.keys(): return False
            store[st] = en
        store = self.sortDict(store)
        intervals = list(store.items())
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]: return False
        return True


    def sortDict(self,dic):
        return {k:v for k,v in sorted(dic.items(),key = lambda z : z[0])}