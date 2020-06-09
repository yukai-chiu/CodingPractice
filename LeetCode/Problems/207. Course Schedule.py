class Solution:
    
    def dfs(self, graph, i):
        #found a cycle
        if self.visited[i] == -1:
            return False
        #we finished it before
        if self.visited[i] == 1:
            return True
        
        self.visited[i] = -1
        for neighbor in graph[i]:
            if not self.dfs(graph,neighbor):
                return False
        self.visited[i] = 1
        return True
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #intuition:
        #finding the cycle in the dependency
        from collections import defaultdict
        graph = defaultdict(list)
        for p in prerequisites:
            nextCourse, prevCourse = p[0], p[1]
            graph[prevCourse].append(nextCourse)
        
        self.visited = [0] * numCourses
        
        for c in range(numCourses):
            if not self.dfs(graph, c):
                return False
        return True
       
            