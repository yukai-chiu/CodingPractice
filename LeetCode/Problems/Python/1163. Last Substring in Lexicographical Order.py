#Brute force
#Time: O(n^2)
#Space: O(n)
class Solution:
    def lastSubstring(self, s: str) -> str:
        if not s:
            return ""
        
        max_sub = 'a'
        last_sub = 0
        for i, ch in enumerate(s):
            if s[i:] > max_sub:
                last_sub = i
                max_sub = s[i:]
        
        return max_sub