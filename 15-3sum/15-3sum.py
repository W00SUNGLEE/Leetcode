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
            #dic[-(nums[i])].append(i)
            if i > 0:
                if nums[i] == nums[i-1]:
                    continue
                    
            #if i+2 < len(nums):
            #    if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 0:
            #        answer.append([0, 0, 0])

                    
            tmp = -(nums[i])
            a = i+1
            b = len(nums)-1
        
            while a < b:
                """
                    if nums[a] == nums[a+1] or nums[b] == nums[b-1]:
                    if nums[a] == nums[a+1]:
                        a += 1
                    if nums[b] == nums[b-1]:
                        b -= 1  
                        
                    if a >= b and nums[a]+nums[b] == tmp:
                        answer.append([nums[i], nums[a], nums[b]])
                    
                    continue
                """

                
                
                
                if nums[a]+nums[b] == tmp:
                    answer.append([nums[i], nums[a], nums[b]])
                    a += 1
                    b -= 1
                    
                elif nums[a]+nums[b] < tmp:
                    a += 1
                elif nums[a]+nums[b] > tmp:
                    b -= 1
            
            
        
        print(answer)
        
        arr = []
        for i in answer:
            if i not in arr:
                arr.append(i)
        return arr
    
        #for i in range(len(answer))
        #    for j in range(i+1, len(answer)):
        