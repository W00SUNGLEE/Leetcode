import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        minPro = sys.maxsize
        
        for price in prices:
            minPro = min(price, minPro)
            maxPro = max(price - minPro, maxPro)
            
        return maxPro