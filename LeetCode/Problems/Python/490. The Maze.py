#My first try:BFS
#Time: O(m*n), size of the maze since we traverse all the maze in worst case
#Space: O(m*n), same as above, we used a visited map 
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        #bfs explore all direction at one
        #use queue
        
        if not maze:
            return False
        
        queue = [tuple(start)]
        visited = set()
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        visited.add(tuple(start))
        
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                for d in direction:
                    new_pos = (curr[0] + d[0],curr[1]+d[1])
                    #trying to reach a wall or edge
                    while 0 <= new_pos[0] < len(maze) and 0 <= new_pos[1] < len(maze[0]) and maze[new_pos[0]][new_pos[1]] == 0: 
                        new_pos = (new_pos[0] + d[0],new_pos[1]+d[1])

                    #reverse back a set
                    new_pos = (new_pos[0] - d[0],new_pos[1]-d[1])
                    if new_pos == tuple(destination):
                        return True
                    if new_pos not in visited:
                        queue.append(new_pos)
                        #print(new_pos)
                        visited.add(new_pos)
        return False
        

#Clean BFS
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze:
            return False
        
        queue = [tuple(start)]
        visited = set()
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        visited.add(tuple(start))
        
        while queue:
                curr = queue.pop(0)
                for d in direction:
                    x = curr[0] + d[0]
                    y = curr[1] + d[1]
                    
                    while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                        x += d[0]
                        y += d[1]       
                    x-=d[0]
                    y-=d[1]

                    if (x,y) == tuple(destination):
                        return True

                    if (x,y) not in visited:
                        queue.append((x,y))
                        visited.add((x,y))
        return False