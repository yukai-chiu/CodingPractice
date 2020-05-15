class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if not arr:
            return False
        
        h = {}
        
        for i in arr:
            if i * 2 in h:
                return True
            elif i % 2 == 0 and i/2 in h:
                return True
            h[i] = i
        return False