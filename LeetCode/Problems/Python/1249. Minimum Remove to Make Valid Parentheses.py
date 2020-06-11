class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #traverse and use stack to store the parantheses,
        #if match, pop from stack
        #at the end, we remove all the remaining parantheses in the stack
        #Time: O(n)
        #Space: O(n) for the stack
        if not s:
            return s
        
        stack = []
        i = 0
        ans = []
        idx_to_remove =set()
        while i < len(s):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    idx_to_remove.add(i)
            i+=1
        
        idx_to_remove = idx_to_remove.union(set(stack))
        
        for i in range(len(s)):
            if i not in idx_to_remove:
                ans.append(s[i])
            
        return "".join(ans)
        