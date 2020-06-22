#Time: O(V+E)
#Space: O(V+E)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
                    

        if len(result) != numCourses:
            return []
        return result