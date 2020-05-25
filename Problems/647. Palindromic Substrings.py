#Brute force
#Time Limit Exceed
#Time: O(n^2 * k)
class Solution:
    def isPalindrome(self, s):
        #O(k), k = lenth of sub string
        for i in range(len(s)//2):
            if s[i] != s[-i -1]:
                return False
        return True
    
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        
        substrings = []
        #O(n^2) calculate all the substrings
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                substrings.append(s[i:j])
        
        ans = 0
        #O(n^2)
        for sub in substrings:
            #O(k)
            if self.isPalindrome(sub):
                ans+=1
                
        return ans

#Expand around center[Accepted]
#Time: O(n^2)
#Space: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        
        ans = 0
        for i in range(len(s)):
            #Odd
            l = r = i
            while l >=0 and r < len(s) and s[l] == s[r]:
                ans+=1
                l-=1
                r+=1
            #Even
            l = i 
            r = i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                ans+=1
                l-=1
                r+=1
                
        return ans