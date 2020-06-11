#Binary search
#Time: O(logn+logm)
#Space: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        
        #binary search row
        l = 0
        r = len(matrix) -1
        row = -1
        while l <= r:
            mid = l + (r-l)//2
            if matrix[mid][0] <= target and matrix[mid][len(matrix[0])-1] >= target:
                row = mid
                break
            elif matrix[mid][0] < target:
                l = mid+1
            else:
                r = mid -1

        if row == -1:
            return False
        
        #binary search col
        l = 0 
        r = len(matrix[0]) -1
        
        while l <= r:
            mid = l + (r - l)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
        
        return False