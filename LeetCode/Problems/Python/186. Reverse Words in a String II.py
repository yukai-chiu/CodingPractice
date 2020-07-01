#Time: O(n)
#Space: O(1)
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)-1
        
        while(l<r):
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
        
        idx = 0
        start = 0
        while idx <= len(s):
            if idx!= len(s) and s[idx] != " ":
                idx+=1
            else:
                end = idx-1
                while start < end:
                    s[start], s[end] = s[end], s[start]
                    start+=1
                    end-=1
                
                idx+=1
                start = idx
                
        
            