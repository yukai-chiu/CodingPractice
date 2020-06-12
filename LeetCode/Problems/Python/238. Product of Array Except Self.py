#Time: O(n)
#Space: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force:
        #iterate and do the calcuation from any index
        #lead to O(n^2)
        
        #method 1, preprocess, and divide by every index value
        #Time: O(n)
        
        #method 2, preprocess from both side, product of all
        #at every index we pick the left and right from each list and multiply them
        n = len(nums)
        forward = [1] * n 
        backward = [1] * n
        forward[0] = 1
        backward[-1] = 1
        for i in range(1,len(nums)):
            forward[i] = forward[i-1] * nums[i-1]
            backward[~i] = backward[~i+1] * nums[~i+1]
        print(forward,backward)
        
        ans = [1] * n
        for i in range(len(nums)):
            ans[i] = forward[i] * backward[i]
        return ans

#My optimization
#Time: O(n)
#Space: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force:
        #iterate and do the calcuation from any index
        #lead to O(n^2)
        
        #method 1, preprocess, and divide by every index value
        #Time: O(n)
        
        #method 2, preprocess from both side, product of all
        #at every index we pick the left and right from each list and multiply them
        n = len(nums)
        forward = 1
        backward = 1
        ans = [1] * n
        for i in range(1,len(nums)):
            
            ans[i] *= forward * nums[i-1]
            ans[~i] *= backward * nums[~i+1]
            forward = forward * nums[i-1]
            backward = backward * nums[~i+1]
            
        print(forward,backward)

        return ans

#two pass clear answer
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force:
        #iterate and do the calcuation from any index
        #lead to O(n^2)
        
        #method 1, preprocess, and divide by every index value
        #Time: O(n)
        
        #method 2, preprocess from both side, product of all
        #at every index we pick the left and right from each list and multiply them
        n = len(nums)


        ans = [1] * n
        for i in range(1,len(nums)):
            #forward pass
            ans[i]*= ans[i-1] * nums[i-1]
        right = 1
        for i in range(len(nums)-1,-1,-1):
            #backward pass
            ans[i] *= right
            right *= nums[i]
            
        #print(ans)
        return ans




#second try
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)


        ans = [1] * n
        for i in range(1,len(nums)):
            #forward pass
            ans[i]*= ans[i-1] * nums[i-1]
        right = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= right
            right *= nums[i]

        return ans