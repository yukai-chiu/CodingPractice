#Stack
#Time: O(n)
#Sapce: O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #stack, between two pops?
        if not s:
            return 0
        
        stack = [-1]
        max_len = 0
        for i, para in enumerate(s):
            if para == "(":
                stack.append(i)
            elif para == ")":
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i-stack[-1])

        return max_len