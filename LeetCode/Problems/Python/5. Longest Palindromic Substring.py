#Time: O(n^2)
#Space: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        max_count = float('-inf')
        left = 0
        right = len(s)
        for i in range(len(s)):
            #Odd
            l = r = i
            count=-1
            while l >=0 and r < len(s) and s[l] == s[r]:
                count+=2
                l-=1
                r+=1
            if count > max_count:
                max_count = max(max_count,count)
                left = l+1
                right = r
                
                
            #Even
            l = i 
            r = i+1
            count = 0
            while l >=0 and r < len(s) and s[l] == s[r]:
                count+=2
                l-=1
                r+=1
            if count > max_count:
                max_count = max(max_count,count)
                left = l+1
                right = r

        return s[left:right]