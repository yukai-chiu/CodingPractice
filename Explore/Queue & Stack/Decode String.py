class Solution:
    def decodeString(self, s: str) -> str:
        
        if not s or len(s) == 0:
            return ""
        
        stack = []
        ans = ""
        
        for i in s:        
            if i == ']':
                curr = stack.pop()
                encoded = ""
                while curr != '[':
                    encoded = curr + encoded
                    curr = stack.pop()            
                k = ""
                while stack and stack[-1].isdigit():
                    curr = stack.pop()
                    k = curr + k     
                stack.append(int(k) * encoded) 
            else:
                stack.append(i)
                
        while stack:
            ans = ans + stack.pop(0)
        return ans