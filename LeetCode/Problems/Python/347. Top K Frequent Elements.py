#Heap
#Time: O(n+klogn)
#Space: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = Counter(nums)
        n = [(-value, key) for key,value in n.items()]
        heapq.heapify(n)
        return [heapq.heappop(n)[1] for _ in range(k)]



#quick select
#Time: O(n) average, worst O(n^2)
#Space: O(n) for hash map and unique elements array
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())
        
        def partition(l, r, pivot):
            pivot_freq = count[unique[pivot]]
            
            #move pivot to end
            unique[pivot], unique[r] = unique[r], unique[pivot]
            
            #move all larger to left
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