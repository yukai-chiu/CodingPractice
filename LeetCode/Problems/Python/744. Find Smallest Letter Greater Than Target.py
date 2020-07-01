class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters)
   
        while l < r:
            mid = l + (r-l)//2
            
            if letters[mid] > target:
                r = mid
            else:
                l = mid+1
        
    
        if l < 0 or l > len(letters)-1:
            return letters[0]
        else:
            return letters[l]