class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = 0
        max_length = 0
        flag = False
        for i in range(len(nums)):
            if nums[i] == 1 and not flag:
                s = i
                flag = True

            elif nums[i] == 0 and flag:
                flag = False
            
            if flag and i - s + 1 > max_length:
                max_length = i - s + 1
                    
        return max_length