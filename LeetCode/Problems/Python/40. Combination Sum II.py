#DFS backtracking 
#Time: O(2^n)
#Space: O(n)
class Solution:
    def dfs(self, candidates, target, result, current):
        #base case: found
        if target == 0:
            result.append(current)
            return
        elif target < 0:
            return
            
        #iterate the candidates    
        for i, c in enumerate(candidates):
            if i == 0 or c != candidates[i-1]:
                self.dfs(candidates[i+1:], target-c, result, current + [c])
        return
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #use dfs with backtracking 
        if not candidates:
            return []
        
        result = []
        candidates.sort()
        #candidates, target, result, current list
        self.dfs(candidates, target, result, [])
        
        return result