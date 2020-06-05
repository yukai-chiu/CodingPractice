class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if not target or '0000' in deadends:
            return -1
        
        
        visited = {}
        num_steps = 0
        queue = ['0000']
        
        while queue:
            
            num_steps +=1
            for i in range(len(queue)):
                curr = queue.pop(0)
                
                for s in range(4):
                    #rotate
                    if int(curr[s]) == 0:
                        move1 = curr[:s] + '9' + curr[s+1:]
                    else:
                        move1 = curr[:s] + str(int(curr[s]) - 1) + curr[s+1:]
                    
                    move2 = curr[:s] + str((int(curr[s]) + 1) % 10) + curr[s+1:]
                   
                    if move1 not in deadends and move1 not in visited:
                        queue.append(move1)
                        visited[move1] = True
                    if move2 not in deadends and move2 not in visited:
                        queue.append(move2)
                        visited[move2] = True
                        
                    if move1 == target or move2 == target:
                        return num_steps
        
        return -1
        
        
        
        
        
        
        
    