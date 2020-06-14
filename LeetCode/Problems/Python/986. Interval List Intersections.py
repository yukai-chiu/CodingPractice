#Two pointers + merge interval
#Time: O(m+n)
#Space: O(1)
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        p1 = 0
        p2 = 0
        
        result = []
        
        while p1 < len(A) and p2 < len(B):
            start = max(A[p1][0], B[p2][0])
            end = min(A[p1][1], B[p2][1])
            if end >= start:
                result.append([start,end])
            
            #move the one that ends earlier
            if A[p1][1] < B[p2][1]:
                p1+=1
            else:
                p2+=1
        
        return result