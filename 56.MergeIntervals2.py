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
        if intervals is None or len(intervals)<=1:
            return intervals

        intervals.sort(key=lambda x:x.start)
        start = intervals[0].start  #因为有赋值，所以前面要加个空值判断
        end  = intervals[0].end
        answer = []
        for interval in intervals:
            if end >= interval.start:   #这个条件下只需更改下end的值就行，不用重新赋值start
                end = max(end, interval.end)
            else:
                answer.append(Interval(start,end))
                start = interval.start
                end = interval.end
        answer.append(Interval(start,end)) 

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