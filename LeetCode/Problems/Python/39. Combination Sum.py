#backtracking 
#Time: O(n^k)
#Space: O(k), when worst case, [1,1,1,1] 4, it will run 4 times recursive
class Solution:
    def dfs(self, candidates, target, result, tempSet, start):
        if target < 0:
            return
        if target == 0:
            result.append(tempSet)
            return
        for i in range(start, len(candidates)):
            self.dfs(candidates, target-candidates[i], result, tempSet+[candidates[i]], i)

        
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        candidates.sort()
        result = []
        self.dfs(candidates, target, result, [], 0)
        return result