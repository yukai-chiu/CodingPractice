#Dynamic Programming
#Time: O(k^2)
#Space: O(k) + O(k) = O(k)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        
        row = [1]
        for r in range(1, rowIndex+2):
            curr_row = [1] * r
            for i in range(r):
                if i != 0 and i != r-1:
                    curr_row[i] = row[i-1] + row[i]
            row = curr_row
        return row

#More memory efficient way
#Dynamic Programming
#Time: O(k^2)
#Space: O(k)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        
        row = []
        for r in range(0, rowIndex+1):
            row.append(1)
            for i in range(len(row)-2, 0, -1):
                row[i] = row[i-1] + row[i]
        return row