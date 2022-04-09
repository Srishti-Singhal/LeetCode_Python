Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals)<2: 
            return intervals
        intervals.sort()
        output = [intervals[0]]
        for start, end in intervals[1:]:
            if start>output[-1][1]:
                output.append([start, end])
            elif end> output[-1][1]:
                output[-1][1]=end
        return output
        