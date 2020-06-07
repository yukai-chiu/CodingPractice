#Brute force
#Time: O(n^2)
#Space: O(1)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #intuition
        #maybe we can caculate the mod of k
        #
        #since it is continuous
        #brute force is to iterate through it
        #prefix sum with hash table?
        #if the mod is the same for prefix sum, there exsits a subarray
        if not nums:
            return False
        
        
        #brute force
        for i in range(len(nums)):
            curr_sum = nums[i]
            for j in range(i+1,len(nums)):
                curr_sum += nums[j]
                if curr_sum == k or (k != 0 and curr_sum %k == 0):
                    return True
        return False