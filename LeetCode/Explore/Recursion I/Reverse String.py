#Old implementation
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) -1
        while(l < r):
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1

#Recursive
#Time: O(n)
#Space: O(n), call stack of recursion
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(l,r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                helper(l+1,r-1)
            
        helper(0,len(s)-1)



#Iterative
#Time: O(n)
#Space: O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) -1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
        