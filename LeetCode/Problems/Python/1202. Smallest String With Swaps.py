class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        #idea is to find overlapping index
        #after we fixed the postion, we can place the connected component in lexicographical order
        class UnionFind:
            def __init__(self, n):
                self.data = [x for x in range(n)]
            
            def union(self, x, y):
                
                self.data[self.find(x)] = self.find(y)
                #print(self.data)
                
            def find(self, x):
                #recursive find the parent
                if x != self.data[x]:
                    self.data[x] = self.find(self.data[x])
                
                return self.data[x]
            
        uf = UnionFind(len(s))
        result = []
        group = defaultdict(list)
        for x,y in pairs:
            uf.union(x,y)
        #form connected component
        for i in range(len(s)):
            group[uf.find(i)].append(s[i])
            
        for comp_id in group.keys():
            #we can reverse sort the list for later pop operation
            group[comp_id].sort(reverse=True)
            #print(group[comp_id])
        
        #iterate build the result
        for i in range(len(s)):
            result.append(group[uf.find(i)].pop())
        #print(group)
        return "".join(result)