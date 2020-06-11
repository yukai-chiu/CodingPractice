#Brute force
#Time: O(n^2)
#Space: O(1)
#Time Limit Exceeded
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #intuition:
        #brute force
        #iterate and find all the possible subarrays
        #Time: O(n^2)
        
        if not nums:
            return 0
        
        ans = 0
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i,len(nums)):
                curr_sum += nums[j]
                if curr_sum == k:
                    ans+=1
        return ans

#Prefix sum hash map
#Time: O(n)
#Space: O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #how about prefix sum to optimize?
        #hash map to store? and everytime we get a new value, we can check
        #if there exsist prefix[curr] - prefix[i] = k
        #then we can know (i,curr) is the desired subarray
        #so what we can do is to check if prefix[curr] - k is in the dict
        
        if not nums:
            return 0
 
        ans = 0
        prefix = {0:1}
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            ans+=prefix.get(curr_sum-k,0)
            prefix[curr_sum] = prefix.get(curr_sum,0)+1

        return ans