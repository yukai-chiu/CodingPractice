class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return s
        
        lookup = {}

        for i in range(len(s)):
            if s[i] not in lookup:
                lookup[s[i]] = i
            else:
                lookup[s[i]] = max(i, lookup[s[i]])
        
        seen = set()
        
        stack = []
        for i in range(len(s)):
            if s[i] not in seen:
                while stack and s[i] <stack[-1] and lookup[stack[-1]] > i:
                    seen.discard(stack[-1])
                    stack.pop()
                seen.add(s[i])
                stack.append(s[i])

        return "".join(stack)