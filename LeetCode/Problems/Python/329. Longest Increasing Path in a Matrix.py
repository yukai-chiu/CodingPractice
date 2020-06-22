class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        def dfs(i,j):
            if memo[i][j] != 0:
                return memo[i][j]
            for d in direction:
                if 0 <= i+d[0] < len(matrix) and 0 <= j+d[1] < len(matrix[0]):
                    if matrix[i+d[0]][j+d[1]] > matrix[i][j]:
                        memo[i][j] = max(memo[i][j], dfs(i+d[0],j+d[1]))
            
            memo[i][j]+=1
            return memo[i][j]
            
        
        
        M = len(matrix)
        N = len(matrix[0])
        memo = [[0] * N  for _ in range(M)]
        longest = 0
        direction = [(1,0), (0,1), (-1,0), (0,-1)]
        
        for i in range(M):
            for j in range(N):
                longest = max(longest, dfs(i,j))
                
        
        return longest


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        in_degree = Counter()
        adj_list = defaultdict(set)
        longest = 0
        direction = [(1,0), (0,1), (-1,0), (0,-1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                in_degree[(i,j)] = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for d in direction:
                    if 0 <= i+d[0] < len(matrix) and 0 <= j+d[1] < len(matrix[0]):
                        if matrix[i+d[0]][j+d[1]] > matrix[i][j]:
                            #can go this way
                            if (i+d[0],j+d[1]) not in adj_list[(i,j)]:
                                in_degree[(i+d[0],j+d[1])]+=1
                                adj_list[(i,j)].add((i+d[0],j+d[1]))
        queue = []
        
        for pos in in_degree:
            if in_degree[pos] == 0:
                queue.append((pos, 1))
        visited = [[0] * len(matrix[0])  for _ in range(len(matrix))]
                
        while queue:
            curr, length = queue.pop()
            longest = max(longest, length)
            visited[curr[0]][curr[1]] = length
            for next_pos in adj_list[curr]:
                #print(next_pos)
                if visited[next_pos[0]][next_pos[1]] < length+1:
                    queue.append((next_pos, length+1))
                        
        
        
        return longest