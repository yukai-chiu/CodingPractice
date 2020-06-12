#Hash map
#Time:O(n)
#Space:O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        for c in count:
            if count[c] > len(nums)//2:
                return c

#Boyer-Moore Voting Algorithm
#Time: O(n)
#Space: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if candidate == n else -1
        return candidate