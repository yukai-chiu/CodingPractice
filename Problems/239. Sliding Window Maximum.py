class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #input check
        if not nums or not k:
            return []
        if k ==1:
            return nums
        
        deq = collections.deque()
        
        #initial
        for i in range(k):
            while deq and nums[i] > nums[deq[-1]]:
                
                deq.pop()
            deq.append(i)

        ans = [nums[deq[0]]]
        #start traverse the list
        
        for i in range(k, len(nums)):
            #print(deq)
            if deq[0] == i-k:
                deq.popleft()
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
            deq.append(i)
            ans.append(nums[deq[0]])
        return ans


#One pass solution deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #input check
        if not nums or not k:
            return []
        if k ==1:
            return nums
        
        deq = collections.deque()
        
        ans = []
        for i,n in enumerate(nums):
            #if the left element is out of bound, pop it
            if i-k >=0 and deq[0] == i-k:
                deq.popleft()
                
            #ensure the queue is DECREASING, we compare the last element and pop all the one smaller than the new one
            #we want to make sure that if the maximum was popped because of out of bound, we still got the second largest
            while deq and n > nums[deq[-1]]:
                deq.pop()    
            deq.append(i)
            
            #we can start to build the answer after k 
            if i>=k-1:
                ans.append(nums[deq[0]])
        
        
        return ans