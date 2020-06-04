class Solution:
    #def schedule(self,step ,costs):
        
        
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        costs.sort(key = lambda x: x[0]-x[1])
        print(costs)
        
        ans = 0
        
        for i in range(len(costs)//2):
            ans += costs[i][0]
            ans += costs[~i][1]
        return ans
        
            