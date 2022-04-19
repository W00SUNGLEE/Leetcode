class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        nums_dic = {}
        print(nums)
        
        i = 0
        while i < len(nums):
            cnt = 1
            for j in range(i+1,len(nums)):
                if nums[i] != nums[j]:
                    break
                else:
                    cnt += 1
            
            print(cnt)
            nums_dic[nums[i]] = nums[i] * cnt
            i += cnt
        
        tmp_key = nums[0]-1
        solution = []
        for key, value in nums_dic.items():
            if key == tmp_key+1:
                solution.append(value)
            else: #key != tmp_key+1
                solution.append(0)
                solution.append(value)
                
            tmp_key = key
        
        print(nums_dic)
        print(solution)
        
        n = len(solution)
        
        if n == 1:
            return solution[0]
        
        else: # n > 1
            dp = [solution[0], max(solution[0], solution[1])]
            
            if n == 2:
                return dp[1]
         
            else: # n > 2
                for i in range(2, len(solution)):
                    dp.append(max(dp[i-1], dp[i-2]+solution[i]))
                
                return dp[n-1] 