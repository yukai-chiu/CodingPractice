class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == None:
            return -1
        m = n = 0
        turn_direction = [[0,1], [1,0]]
        walk_direction = [[-1,1], [1,-1]]
        t = w = 0
        result = []
        while m < len(matrix) and n < len(matrix[0]):
            result.append(matrix[m][n])
            m += walk_direction[w][0]
            n += walk_direction[w][1]
            if w == 0:
                if m  < 0 and n < len(matrix[0]):
                    m += 1
                    # += 1
                    w = 1
                elif n >= len(matrix[0]):
                    m += 2
                    n -= 1
                    w = 1
            elif w == 1:
                if n < 0 and m < len(matrix):
                    # += 1
                    n += 1
                    w = 0
                elif m >= len(matrix):
                    m -= 1
                    n += 2
                    w = 0
        return result

                
            