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
        
#quick select
#Time: O(n) in average case, O(n^2) worst case
#Space: O(n)      
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())
        
        def partition(l, r, pivot):
            pivot_freq = count[unique[pivot]]
            
            #move pivot to end
            unique[pivot], unique[r] = unique[r], unique[pivot]
            
            #move all smaller to left
            store_idx = l
            for i in range(l,r):
                if count[unique[i]] > pivot_freq:
                    unique[store_idx], unique[i] = unique[i], unique[store_idx]
                    store_idx+=1
            #put pivot to the correct idx
            unique[store_idx], unique[r] = unique[r], unique[store_idx]
            
            return store_idx
            
        def quickSelect(left, right, k):
            #base case: only one element
            if left == right:
                return
            
            #select a pivot
            pivot_idx = random.randint(left, right)
            
            #find the pivot position in a sorted list
            pivot_idx= partition(left, right, pivot_idx)
            
            if pivot_idx == k:
                return
            elif pivot_idx > k:
                quickSelect(left, pivot_idx-1, k)
            else:
                quickSelect(pivot_idx+1, right, k)
        
        
        n = len(unique)
        quickSelect(0, n-1, k)
        

        return unique[:k]