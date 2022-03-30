class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        List = []
        
        for i in range(len(accounts)):
            cnt = 0
            for j in range(len(accounts[i])):
                cnt += accounts[i][j]
                
            List.append(cnt)
        
        return max(List)
                
            