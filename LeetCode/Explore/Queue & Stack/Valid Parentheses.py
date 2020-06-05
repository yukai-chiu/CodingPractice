class Solution:
    def isValid(self, s: str) -> bool:
        if not s or s =="":
            return True
        
        
        stack = []
        
        for pare in s:
            if pare in ['(', '{', '[']:
                stack.append(pare)
            else:
                if not stack:
                    return False
                curr = stack.pop()
                if curr + pare not in ['()','{}','[]']:
                    return False
        
        return True if len(stack) == 0 else False
        
        