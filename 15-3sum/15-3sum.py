from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        answer = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                    
            tmp = -(nums[i])
            a = i+1
            b = len(nums)-1
        
            while a < b:              
                numSum = nums[a]+nums[b]
                if numSum == tmp:
                    answer.append([nums[i], nums[a], nums[b]])
                    a += 1
                    b -= 1
                    while nums[a] == nums[a-1] and a < b:
                        a += 1
                    
                elif numSum < tmp:
                    a += 1
                elif numSum > tmp:
                    b -= 1
            

        print(answer)

        return answer

        