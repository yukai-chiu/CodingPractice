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



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []
        
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        result = []
        
        
        for interval in intervals[1:]:
            if interval[0] > end:
                result.append([start,end])
                start = interval[0]
            end = max(end, interval[1])
            #else:
            #    end = interval[1]
        if not result or start > result[-1][1]:
            result.append([start,end])
        
        
        return result