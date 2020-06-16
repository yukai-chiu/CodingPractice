#Time: O(n)
#Space: O(n)
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        #build the list
        s = [(c, i) for i, c in enumerate(start) if c == 'L' or c == 'R']
        e = [(c, i) for i, c in enumerate(end) if c == 'L' or c == 'R']
        #print(s, e)
        
        if len(s) != len(e):
            return False
        for (c1, i1), (c2, i2) in zip(s,e):
            if c1 == c2:
                if c1 == 'L':
                    if not i1 >= i2:
                        return False
                
                if c2 == 'R':
                    if not i2 >= i1:
                        return False               
            else:
                return False       
        return True
