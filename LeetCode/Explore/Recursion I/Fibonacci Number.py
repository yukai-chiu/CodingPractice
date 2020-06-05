#Recursive
#Time: O(2^N)
#Space: O(N)
class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        return self.fib(N-1) + self.fib(N-2)

#Recursive + Memoization
#Time: O(N)
#Space: O(N)
class Solution:
    def fib(self, N: int) -> int:
        memo = {}
        
        def helper(N):
            if N < 2:
                return N
            if N in memo:
                return memo[N]
            else:
                memo[N] = helper(N-1) + helper(N-2)
                return memo[N]
        
        return helper(N)

#Iterative
#Time: O(N)
#Space: O(1)
class Solution:
    def fib(self, N: int) -> int:
        memo = [0] * 3
        memo[1] = 1
        if N < 2:
            return N
        
        for i in range(2, N+1):
            memo[2] = memo[0] + memo[1]
            #swap
            memo[0] = memo[1]
            memo[1] = memo[2]
        
       
        return memo[2]