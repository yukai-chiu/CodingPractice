#Two pointers
#Time: O(n)
#Space: O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        #brute force:
        #list all the n possibilities and check them
        #will lead to Time: O(n^2)
        #and Space: O(n)
        
        #can we use two pointer and remove the first one that's not match?
        # but in this case: abbbbca, we don't know should we remove b or c
        #if we start from the middle?
        def isPalindrome(s):
            if not s or len(s)==1:
                return True
            for i in range(len(s)//2):
                if s[i] != s[~i]:
                    return False
                
            return True
        
        if not s or len(s)==1:
            return True
    
        l = 0
        r = len(s) -1
        while l < r:
            if s[l]!=s[r]:
                return isPalindrome(s[:l]+s[l+1:]) or isPalindrome(s[:r] + s[r+1:])
            
            l+=1
            r-=1
        return True