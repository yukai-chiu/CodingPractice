class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) ==1:
            return True
        #brute force:
        #traverse from front and back, compare with reversed
        #if not match, return False
        
        #Better way, two pointer, compare each iteration
        #if l == r, return True
        #we need to bypass all the char except alphanumeric 
        l = 0
        r = len(s)-1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l+=1
            while l < r and not s[r].isalnum():
                r-=1
            #print(s[l],s[r])
            if s[l].lower() != s[r].lower():
                return False
            
            l+=1
            r-=1
        
        
        return True
        
        