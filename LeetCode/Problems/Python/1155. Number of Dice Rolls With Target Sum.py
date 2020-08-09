#Recursion + memo
#Time : O(f*d*target)
#Space: O(d*target)
class Solution:
    def rolldice(self, idx, f, target, memo):
        if idx ==0 and target == 0:
            return 1
        elif idx==0 or target < 0:
            return 0
        
        if (idx, target) in memo:
            return memo[(idx,target)]
        
        count = 0
        for i in range(1, f+1):
            count+=self.rolldice(idx-1, f, target-i, memo)
        memo[(idx, target)] = count
        
        return memo[(idx, target)]    
        
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        return self.rolldice(d, f, target, {}) % (10**9 + 7)

#dynamic programming
#Time : O(f*d*target)
#Space: O(target)
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        prev = [0] * (target+1)
        prev[0] = 1
        for i in range(d):
            curr = [0] * (target+1)
            for j in range(1,f+1):
                for k in range(j,target+1):
                    curr[k] = (curr[k]+prev[k-j])
            prev = curr.copy()
            
        return prev[target]% (10**9+7)