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
            