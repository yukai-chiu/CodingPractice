#Time: O(n)
#Space: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        last = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= last:
                last = i
        return last == 0

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        buffer = 0
        for n in nums[:-1]:
            buffer-=1
            if n <=0:
                if buffer <= 0:
                    return False
            else:
                buffer = max(buffer,n)
        return True