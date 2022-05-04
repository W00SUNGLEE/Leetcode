class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        print(nums)
        answer = [-1, -1]
        
        for i in range(len(nums)):
            if nums[i] == target:
                if answer[0] == -1:
                    answer = [i, i]
                else:
                    answer[1] = i
                    
        print(answer)
        return answer
                