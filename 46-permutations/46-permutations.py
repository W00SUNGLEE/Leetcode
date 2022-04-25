class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        solution = []
        
        tmp = []
        
        def backtracking(v):
            if v == len(nums):
                solution.append([i for i in tmp])
                
            else:
                for i in range(len(nums)):
                    if nums[i] not in tmp:
                        tmp.append(nums[i])
                        backtracking(v+1)
                        tmp.pop()
                        
        backtracking(0)
        
        return solution
        