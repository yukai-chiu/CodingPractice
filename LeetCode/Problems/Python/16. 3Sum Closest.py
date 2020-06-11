#My first try
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #similar idea to 3Sum but we are exploring all the combinations
        #and maintain a closest value
        if not nums:
            return None
        nums.sort()
        closest = float('inf')
        ans = [0,0,0]
        for i, n in enumerate(nums):
            l = i+1
            r = len(nums)-1
            while l < r:
                if abs(target - (n+nums[l]+nums[r])) < closest:
                    closest = abs(target - (n+nums[l]+nums[r]))
                    ans = [i,l,r]
                if n+nums[l]+nums[r] == target:
                    return nums[i]+nums[l]+nums[r]
                elif n+nums[l]+nums[r] < target:
                    l+=1
                elif n+nums[l]+nums[r] > target:
                    r-=1
        return nums[ans[0]]+nums[ans[1]]+nums[ans[2]]

#Clean code
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #similar idea to 3Sum but we are exploring all the combinations
        #and maintain a closest value
        if not nums:
            return None
        nums.sort()
        diff = float('inf')
        for i, n in enumerate(nums):
            l = i+1
            r = len(nums)-1
            while l < r:
                sum = n+nums[l]+nums[r]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    l+=1
                else:
                    r-=1
            if diff == 0:
                break
        return target - diff