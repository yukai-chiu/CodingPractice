#Brute force
#Time: O(2^n), at each step we go through 2 branches.
#Space: O(n), depth of recursion tree can go up to n in the call stack
class Solution:
    def climb_stairs(self, i, target):
        #if we land over the target, means it's not a solution
        if i > target:
            return 0
        #if we land at the target stair, means we found a solution
        if i == target:
            return 1
        #take a step, walk 1 or 2 stairs. Calculate all the combinations
        return self.climb_stairs(i + 1, target) + self.climb_stairs(i + 2, target)
        
    def climbStairs(self, n: int) -> int:
        if not n or n == 0:
            return 0
        
        return self.climb_stairs(0, n)
        
#memoization
#use memo array to store all the caculated result
#so we can reference it later, no need to recaculate
#prune the recursion tree
#Time: O(n), since we now only need to calcuate once for every i 
#Space: O(n), still up to n recursion, and memo size is n
class Solution:
    def climb_stairs(self, i, target, memo):
        if i > target:
            return 0
        if i == target:
            return 1
        
        if memo[i] != 0:
            return memo[i]
        
        memo[i] = self.climb_stairs(i + 1, target, memo) + self.climb_stairs(i + 2, target, memo)
        
        return memo[i]
        
    def climbStairs(self, n: int) -> int:
        if not n or n == 0:
            return 0
        memo = [0] * n
        return self.climb_stairs(0, n, memo)


#dynamic programming
#Time: O(n)
#Space: O(n)
class Solution:      
    def climbStairs(self, n: int) -> int:
        if not n or n == 0:
            return 0
        if n == 1:
            return 1
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]



#Fibonacci Number
#Time: O(n)
#Space: O(1)
class Solution:      
    def climbStairs(self, n: int) -> int:
        if not n or n == 0:
            return 0
        if n == 1:
            return 1
        
        a1 = 1
        a2 = 2
        
        for i in range(2, n):
            a3 = a1 + a2 # a_i = a_i-1 + a_i-2
            a1, a2 = a2, a3 #switch
        
        return a2
        