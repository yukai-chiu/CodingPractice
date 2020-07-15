#Time: O(max(m,n))
#Space: O(1)
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        edited = False
        
        ptr_s = 0
        ptr_t = 0
        if s == t or abs(len(s) - len(t)) >=2:
            return False
        
        while ptr_s < len(s) and ptr_t < len(t):
            if s[ptr_s] != t[ptr_t]:
                if not edited:
                    edited = True
                else:
                    return False
                if len(s) > len(t):
                    ptr_t-=1
                if len(s) < len(t):
                    ptr_s-=1
            ptr_s+=1
            ptr_t+=1

        return True