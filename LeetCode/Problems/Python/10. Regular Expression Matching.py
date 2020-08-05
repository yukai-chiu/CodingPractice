#recursion + memo
#Time: O(t*p)
#Space: O(t*p)
class Solution:
    def matching(self, s, p, s_i, p_i, memo):
        if (s_i, p_i) in memo:
            return memo[(s_i, p_i)]
        if p_i == len(p):
            ans = s_i == len(s)
        else:
            first_match = s_i < len(s) and p[p_i] in {s[s_i], '.'}
            if len(p) >=p_i+2 and p[p_i+1] == '*':
                #skip pattern or match pattern
                ans = self.matching(s, p, s_i, p_i+2, memo) or (first_match and self.matching(s, p, s_i+1, p_i, memo))

            #not *
            else:
                ans = first_match and self.matching(s, p, s_i+1, p_i+1, memo)
        
        memo[(s_i, p_i)] = ans
        return memo[(s_i, p_i)]
        
    def isMatch(self, s: str, p: str) -> bool:
        if (not s and not p) or s==p:
            return True
        
        
        return self.matching(s, p, 0, 0, {})

#recursion
#Time: O(2^(T+P/2))
#Space: O(T^2+P^2)
class Solution:
    def matching(self, s, p, s_i, p_i):
        if p_i >= len(p):
            return s_i == len(s)
        
        #print(s_i, p_i, s[s_i], p[p_i])
        first_match = s_i < len(s) and p[p_i] in {s[s_i], '.'}
       
        
        if len(p) >=p_i+2 and p[p_i+1] == '*':
            #skip pattern or match pattern
            return self.matching(s, p, s_i, p_i+2) or (first_match and self.matching(s, p, s_i+1, p_i))
       
        #not *
        else:
            return first_match and self.matching(s, p, s_i+1, p_i+1)
        
        
        
    def isMatch(self, s: str, p: str) -> bool:
        if (not s and not p) or s==p:
            return True
        
        
        return self.matching(s, p, 0, 0)