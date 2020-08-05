#hashmap
#Time: O(n)
#Space: O(n)
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if not nums or k < 0:
            return 0
        
        unique = Counter(nums)
        result = 0
    
        for n in unique:
            if k>0 and n-k in unique:
                result+=1
            elif k==0 and unique[n] >1:
                result+=1
                
        return result


#Sort + hashmap
#Time: O(nlogn)
#Space: O(n)
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        nums.sort()
        seen = set()
        ret = set()
        
        for n in nums:
            if n-k in seen:
                ret.add((n-k, n))
            seen.add(n)
        return len(ret)