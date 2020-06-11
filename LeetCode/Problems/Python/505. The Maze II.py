#BFS
#Time: O(m*n * max(m,n))
#Space: O(m*n)
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if not maze:
            return -1
        if start == destination:
            return 0
        
        visited = {}
        queue = [(tuple(start), 0)]
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        min_path = float('inf')
        while queue:
            s, steps = queue.pop(0)
            
            for d in direction:
                curr_step = steps
                x = s[0] + d[0]
                y = s[1] + d[1]
                curr_step+=1
                #roll until we hit the wall or border
                while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                    x += d[0]
                    y += d[1]
                    curr_step+=1
                    
                x -= d[0]
                y -= d[1]
                curr_step-=1
                
                if (x,y) == tuple(destination):
                    min_path = min(curr_step,min_path)
                
                if (x,y) not in visited:
                    visited[(x,y)] = curr_step
                    queue.append(((x,y),curr_step))
                else:
                    if visited[(x,y)] > curr_step:
                        visited[(x,y)] = curr_step
                        queue.append(((x,y),curr_step))
                
                    
        return min_path if min_path != float('inf') else -1
        
                
            
        
        