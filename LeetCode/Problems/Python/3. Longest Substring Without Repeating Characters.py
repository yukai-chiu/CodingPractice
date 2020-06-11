#First try
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_pos = 0
        end_pos = 0
        max_count = 0

        
        for idx, ch in enumerate(s):
            if ch not in s[start_pos:idx]:
                end_pos = idx
            
            elif ch in s[start_pos:idx]:
                while(ch in s[start_pos:idx]):
                    start_pos +=1
                end_pos = idx
            
            if(end_pos - start_pos + 1 > max_count):
                max_count = end_pos - start_pos + 1
                
        
        return max_count

#hash map
#Time: O(n)
#Space: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        lookUp = {}
        longest = 0
        start = 0
        for i,c in enumerate(s):
            if c in lookUp:
                #we only look at the current window, it could be smaller than start
                start = max(start,lookUp[c]+1)
                
            longest = max(longest, i - start+1)  
            #set to the latest
            lookUp[c] = i
        

        return longest