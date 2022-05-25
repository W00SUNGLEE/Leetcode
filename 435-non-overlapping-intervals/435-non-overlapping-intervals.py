import sys
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        print(intervals)
        n = len(intervals)
        answer = 0
        dp = -(sys.maxsize)  
        
        for s, e in intervals:
            if s < dp:
                answer += 1
                dp = min(dp, e)
                
            else:
                dp = e
                
        return answer