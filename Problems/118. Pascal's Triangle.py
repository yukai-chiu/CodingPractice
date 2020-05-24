#Dynamic Programming
#Time: O(numRows^2)
#Space: O(numRows^2)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows or numRows == 0:
            return []
        
        pascal = []
        
        for r in range(1, numRows+1):
            row = [1] * r
            for i in range(r):
                if i != 0 and i != r-1:
                    row[i] = pascal[-1][i-1] + pascal[-1][i]  
            pascal.append(row)
        
        return pascal
                    