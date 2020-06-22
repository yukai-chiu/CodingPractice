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

 #topological sort      
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return False
        in_degree = Counter()
        for i in range(numCourses):
            in_degree[i] = 0
            
        adj_list = defaultdict(set)
        for p in prerequisites:
            if p[0] not in adj_list[p[1]]:
                adj_list[p[1]].add(p[0])
                in_degree[p[0]]+=1

        deq = deque()
        for i in in_degree:
            if in_degree[i] == 0:
                deq.append(i)
        result = []
        while deq:
            curr = deq.popleft()
            result.append(curr)
            for adj in adj_list[curr]:
                in_degree[adj]-=1
                if in_degree[adj]==0:
     
                    deq.append(adj)
                    

        
        return len(result) == numCourses