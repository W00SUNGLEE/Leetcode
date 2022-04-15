class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        
        if len(cost) == 2:
            return min(cost[0], cost[1])
        
        else:
            cost.append(0)
            dp = [cost[0], cost[1]]
        
            for i in range(2, len(cost)):
                dp.append(min(dp[i-2] + cost[i], dp[i-1] + cost[i]))
        
            return dp[len(cost) - 1]