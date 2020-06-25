#min max heap
#Time: O(logn)
#Space: O(n)
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []
        self.hi = []
        self.n = 0

    def addNum(self, num: int) -> None:
   
        self.n+=1
 
        if self.n % 2 == 1:
            if self.hi and num > self.hi[0]:
                heapq.heappush(self.hi, num)
                temp = heapq.heappop(self.hi)
                heapq.heappush(self.lo,-temp)
            else:
                heapq.heappush(self.lo,-num)   
        else:
            if self.hi and num > self.hi[0]:
                heapq.heappush(self.hi,num)
            else:
                heapq.heappush(self.lo, -num)
                temp = heapq.heappop(self.lo)
                heapq.heappush(self.hi,-temp)   
                
        

    def findMedian(self) -> float:
        if self.n % 2 ==1:
            return -self.lo[0]
        else:
            return (-self.lo[0] + self.hi[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()