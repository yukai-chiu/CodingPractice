#First Try
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if(len(nums)<3):
            return []
        nums.sort()
       
        results = []
        for i in range(len(nums)-2):
            if(nums[i] > 0 ):
                break
                
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            l = i+1
            r = len(nums) -1
            while(l<r):
                temp_sum = nums[l] + nums[r] + nums[i]
                if(temp_sum <0):
                    l+=1
                elif(temp_sum >0):
                    r-=1
                else:
                    results.append([nums[i],nums[l],nums[r]])
                    while(l < r and nums[l] == nums[l+1]):
                        l+=1
                    while(l < r and nums[r] == nums[r-1]):
                        r-=1
                    l+=1
                    r-=1
        return results


#Two pointer
#Time: O(n^2)
#Space: O(n) if not sorted inplace
#we ignore the space for output
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        #sort the list first
        #iterate from the start
        #if it is same as the previous, skip it
        #use two pointers on every iteration
        #can solve it in O(n^2)
        
        ans = []
        nums.sort()
        
        for i,n in enumerate(nums):
            #don't need to handle if n > 0, sum will never be 0
            if n >0:
                break
            #bypass duplicated value
            if i >0 and n == nums[i-1]:
                continue
   
            l = i+1
            r = len(nums) - 1
            
            while l < r:
                curr_sum = nums[l] + nums[r] + n
                if curr_sum == 0:
                    ans.append([n,nums[l],nums[r]])
                    l+=1
                    r-=1
                    #bypass duplicated value
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                elif curr_sum > 0:
                    r-=1
                elif curr_sum < 0:
                    l+=1
        return ans  
                        
                    
            
        