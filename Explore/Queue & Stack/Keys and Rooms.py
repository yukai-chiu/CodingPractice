class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        if not rooms:
            return False
        
        visited = [0 for _ in rooms]
        queue = [rooms[0]]
        visited[0] = 1
        #dfs
        while queue:
            keys = queue.pop(0)
            for k in keys:
                if visited[k] == 0:
                    visited[k] = 1
                    queue.append(rooms[k])   
                    
        return all(visited) == 1