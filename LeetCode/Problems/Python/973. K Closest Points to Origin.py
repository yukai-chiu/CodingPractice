#Time: O(nlogn)
#Space: O(n)
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        
        for idx, pt in enumerate(points):
            if len(heap) >= K:
                heapq.heappushpop(heap, (-(pt[0]**2+pt[1]**2), idx))
            else:
                heapq.heappush(heap, (-(pt[0]**2+pt[1]**2), idx))    
       
        result = []
        for _,idx in heap:
            result.append(points[idx])
            
        return result