#My first try: heap
#Time: O(nlogn)
#Space: O(n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heap = []
        for i in intervals:
            heapq.heappush(heap, (i[0],-1))
            heapq.heappush(heap, (i[1],1))
        
        conti = 0
        result = []
        start = 0
        end = 0
        while heap:
            curr = heapq.heappop(heap)
            conti+=curr[1]
            if conti == -1 and curr[1]==-1:
                start = curr[0]
            if conti == 0:
                end = curr[0]
                result.append([start,end])
                #print([start,end])
        
        return result