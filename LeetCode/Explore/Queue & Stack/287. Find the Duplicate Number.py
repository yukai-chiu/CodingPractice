#Time: O(n)
#Space: O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        slow = nums[0]
        fast = nums[0]
        start = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
 
        while start != slow:
            slow = nums[slow]
            start = nums[start]
        
        return start