#Prefix sum with linear search
#Time: O(n) for init
#      O(n) for pickIndex
#Space:O(n) to store the prefix sum
#Space:O(1) for pickIndex
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        self.total = 0
        
        for weight in w:
            self.total += weight
            self.prefix.append(self.total)
        

    def pickIndex(self) -> int:
        
        target = self.total *random.random()
        for i,w in enumerate(self.prefix):
            if target<w:
                return i
        
        

#Prefix sum with binary search
#Time: O(n) for init
#      O(logn) for pickIndex
#Space:O(n) to store the prefix sum
#Space:O(1) for pickIndex

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        self.total = 0
        
        for weight in w:
            self.total += weight
            self.prefix.append(self.total)
        

    def pickIndex(self) -> int:
        
        target = self.total *random.random()
        
        mid = len(self.prefix)//2
        l = 0
        r = len(self.prefix)
        #we are finding the edge bewteen l and r
        #if l = mid+1 = r then we find it
        #cause we want to find a point that the previous is smaller than target 
        #but next one larger than target
        while l<r:
            mid = l + (r-l)//2
            if self.prefix[mid] < target:
                l = mid+1
            else:
                r = mid
                
        
        return l