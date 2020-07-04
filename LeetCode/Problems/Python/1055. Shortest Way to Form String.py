#First try two pointer
#Time: O(m*n)
#Space:O(m)
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if not source or not target:
            return -1
        
        ptr_s = 0
        ptr_t = 0
        
        result = 0
        unique = set(source) 

        while ptr_t < len(target):
            if target[ptr_t] not in unique:
                return -1
            
            if source[ptr_s] != target[ptr_t]:
                ptr_s+=1
                
            else:
                ptr_s+=1
                ptr_t+=1
                
            if ptr_s == len(source) or ptr_t == len(target):
                ptr_s = 0
                result+=1
        return result