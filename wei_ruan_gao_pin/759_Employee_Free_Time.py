"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        
        for i in range(len(schedule)):
            for j in range(len(schedule[i])):
                intervals.append([schedule[i][j].start,schedule[i][j].end])
        intervals.sort()
        common = []
        for x,y in intervals:
            if not common or common[-1][1]<x:
                common.append([x,y])
            else:
                common[-1][1]=max(y,common[-1][1])
        output = []
        for i in range(1,len(common)):
            output.append(Interval(common[i-1][1],common[i][0]))
        return output
