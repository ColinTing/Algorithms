# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        answer = []

        for interval in sorted(intervals,key=lambda k: k.start):
            if not answer or answer[-1].end<interval.start:
                answer.append(interval)
            else:
                answer[-1].end = max(interval.end, answer[-1].end)

        return answer
        




interval1 =  Interval(1,3)
interval2 =  Interval(2,6)
interval3 =  Interval(8,10)
interval4 =  Interval(15,18)

intervals= []
intervals.append(interval1)
intervals.append(interval2)
intervals.append(interval3)
intervals.append(interval4)
s = Solution().merge(intervals)
print(intervals[0].start)
print(intervals[0].end)
