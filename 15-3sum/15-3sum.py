from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        
        answer = []
        #dic = defaultdict(list)
        if len(nums) < 3:
            return answer
        
        if len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                return [[nums[0], nums[1], nums[2]]]
            else:
                return answer
                    
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                    
            tmp = -(nums[i])
            a = i+1
            b = len(nums)-1
        
            while a < b:              
                if nums[a]+nums[b] == tmp:
                    answer.append([nums[i], nums[a], nums[b]])
                    a += 1
                    b -= 1
                    while nums[a] == nums[a-1]and a < b:
                        a += 1
                    
                elif nums[a]+nums[b] < tmp:
                    a += 1
                elif nums[a]+nums[b] > tmp:
                    b -= 1
            

        print(answer)

        return answer

        