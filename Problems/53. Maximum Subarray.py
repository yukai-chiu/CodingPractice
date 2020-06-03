#Time: O(n)
#Space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_sum = float('-inf')
        curr_sum = float('-inf')
        for n in nums:
            curr_sum = max(n, curr_sum + n)
            max_sum = max(max_sum, curr_sum)
        
        return max_sum

#Time: O(n)
#Space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_sum = float('-inf')
        for i in range(1, len(nums)):
            #restart if local maximum < 0, just drop them
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_sum = max(max_sum, nums[i])
        return max_sum
                

def largestSum(input):
    

    if not input:
        return None

    largest = float('-inf')
    r = 0 
    l = 0
    current_sum = 0
    
    
    """for i in range(len(input)):
        #start a new subarray or continue
        current_sum = max(current_sum + input[i], input[i])
        largest = max(current_sum, largest)"""
    
    while r < len(input):
        #calculate current sum
        
        #temp_r = r 
        #temp_l = l
        while r < len(input) and input[r] < current_sum + input[r]:
            current_sum += input[r]
            print("Add:",r,input[r], current_sum)
            if current_sum > largest:
                largest = current_sum
            
            r+=1
        
        
        while l < r:# and current_sum < current_sum - input[l]:
            
            current_sum -= input[l]
            print("Drop:" , l , input[l], current_sum)
            if current_sum > largest:
                largest = current_sum
            l+=1

        
        if current_sum > largest:
            largest = current_sum

        #current_sum += input[r]
        #current_sum -= input[l]
        
        #l+=1
        if r < len(input):
            current_sum = input[r]
            print("Add:",r,input[r], current_sum)
            l = r
            r+=1