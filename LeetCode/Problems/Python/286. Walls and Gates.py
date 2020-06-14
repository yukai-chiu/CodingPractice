#BFS, find gates first, can avoid recalculation
#Time: O(m*n)
#Space:O(m*n)
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        #traverse room, find 0, and start doing bfs
        #update with min distance
        
        if not rooms:
            return
        
        row = len(rooms)
        col = len(rooms[0])
        queue = []
        def bfs():
            
            directions = [[0,1], [1,0], [-1,0], [0,-1]]
            
            while queue:
                i, j = queue.pop()
                #search neighbor
                for d in directions:
                    new_i = i+d[0]
                    new_j = j+d[1]
                    if 0<=new_i<row and 0<=new_j<col and rooms[new_i][new_j]!= -1:
                        #update
                        if rooms[i][j]+1 < rooms[new_i][new_j]:
                            rooms[new_i][new_j] = rooms[i][j]+1
                            queue.append([new_i,new_j])

        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    queue.append([i,j])
        bfs()
                    