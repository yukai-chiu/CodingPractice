class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #intuition:
        #sort it? and access the k element?
        #Time: O(nlogn)
        #Space: O(1)
        nums.sort()
        
        return nums[-k]
        
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #min heap
        #Time: O(n)
        heapq.heapify(nums)
        #Time: [theta(1) or O(logn)] * (n-k) 
        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]
        
        