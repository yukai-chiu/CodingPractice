class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        count = Counter(s)
        
        for c in s:
            if count[c] % 2 == 0:
                del count[c]
               
            
        
        return len(count) <=1