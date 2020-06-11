#Binary search on every row or col
#Time: O(nlogm or mlogn)
#Space: O(1)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        if len(matrix) < len(matrix[0]):
            for row in matrix:
                lo = 0
                hi = len(row)-1
                while lo <= hi:
                    mid = lo + (hi-lo)//2
                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        lo = mid+1
                    else:
                        hi = mid-1
                        
                
        else:
            for col in zip(*matrix):
                lo = 0
                hi = len(col)-1
                while lo <= hi:
                    mid = lo + (hi-lo)//2
                    if col[mid] == target:
                        return True
                    elif col[mid] < target:
                        lo = mid+1
                    else:
                        hi = mid-1
        
        return False

#reduced search space
#Time: O(m+n)
#Space: O(1)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        row = len(matrix)-1
        col = 0
        
        while row >=0 and col < len(matrix[0]):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col+=1
            else:
                row-=1
        
        return False