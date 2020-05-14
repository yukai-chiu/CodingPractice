class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return 0
        
        result = []
        i = 0
        while i < len(A) and A[i] < 0:
            i += 1
        j = i - 1
        
        while j >= 0 and i < len(A):
            if A[j]**2 > A[i]**2:
                result.append(A[i]**2)
                i+=1
            else:
                result.append(A[j]**2)
                j-=1
        while j >= 0:
            result.append(A[j]**2)
            j-=1
                
        while i < len(A):
            result.append(A[i]**2)
            i+=1
        return result