class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
    
        n = len(values)
    
        dp = []
        maxValue = max(values[0], values[1]+1)
        dp.append(0)
        dp.append(values[0]+values[1]-1)

    
        for i in range(2, n):
            dp.append(max(dp[i-1], maxValue+values[i]-i))
            maxValue = max(maxValue, values[i]+i)
            
        answer = dp[-1]
        
        return answer
        