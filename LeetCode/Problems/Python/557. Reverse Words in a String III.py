class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        
        result = []
        for w in s.split(" "):
            result.append(w[::-1])
            
        return " ".join(result)