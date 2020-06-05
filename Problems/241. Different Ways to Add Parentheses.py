class Solution:
    def diffWays(self,s, memo):
        if s.isdigit():
            return [int(s)]
        res = []
        
        #check if exists in memo to reduce duplicated computation
        if s in memo:
            return memo[s]
        
        for i, c in enumerate(s):
            #if we found an operator, split it and do the recusion
            #this is the same behavior of using parenthesis
            if c in "+-*":
                front = self.diffWays(s[:i], memo)
                back = self.diffWays(s[i+1:], memo)
                #caculate all the possible combinations
                for x in front:
                    for y in back:
                        res.append(self.helper(x,y,c))
        #store in memo
        memo[s] = res
        return memo[s]
                
    def helper(self,x,y,c):             
        if c == "+":
            return x+y
        elif c == "-":
            return x-y
        elif c == "*":
            return x*y
                
    def diffWaysToCompute(self, input: str) -> List[int]:
        #intuition:
        #since we are searching all the possible way
        #try recursion
        #observation: pair will be the same as operator
        #divide and recusion at every operator
        
        if not input:
            return []
        
        ans = self.diffWays(input,{})
        
        return ans
        
                
        