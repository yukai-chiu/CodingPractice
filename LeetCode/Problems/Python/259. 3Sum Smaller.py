class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        nums.sort()
        result = 0
        for i, n in enumerate(nums):
            l = i+1
            r = len(nums)-1
            prev = None
            while l < r:
                sum = n + nums[l] + nums[r]
                if sum < target:
                    curr_r = r
                    while l < curr_r:
                        result+=1
                        curr_r-=1
                    l+=1
                elif sum >= target:
                    r-=1

        return result