class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        seen = [len(matrix[0])* [False] for _ in matrix ]
        d_list = [[0,1],[1,0],[0,-1],[-1,0]]
        m = n = d = 0      
        result = []
        while len(result) < len(matrix) * len(matrix[0]):
            result.append(matrix[m][n])
            seen[m][n] = True
            next_m = m + d_list[d][0]
            next_n = n + d_list[d][1]
            if 0 <= next_m < len(matrix) and 0 <= next_n < len(matrix[0]) and not seen[next_m][next_n]:
                m = next_m
                n = next_n
            else:
                d = (d + 1) % 4
                m += d_list[d][0]
                n += d_list[d][1]
        return result
        