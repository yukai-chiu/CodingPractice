#Sliding window
#Time: O(T+S), 2*S + T
#Space: O(T+S)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        if s == t:
            return s
        
        lookup = Counter(t)
        #initial
        curr_window = Counter()  
        
        l = 0
        r = 0
        found = 0
        min_window = (float('inf'), l, r)
        #r move to find valid window
        while r < len(s):
            #move right pointer one step and check if satisfy substring
            if r < len(s) and found < len(lookup):
                curr_window[s[r]] = curr_window.get(s[r], 0)+1
                if s[r] in lookup and curr_window[s[r]] == lookup[s[r]]:
                    found +=1
            
            #once we found, move left pointer as much as we can until it's not match the requirement
            while l < len(s) and found == len(lookup):
                curr_window[s[l]] -=1
                #update min window
                if min_window[0] > r-l+1:
                    min_window = (r-l+1, l, r)
                if s[l] in lookup and curr_window[s[l]] < lookup[s[l]]:
                    found-=1
                l+=1
  
            r+=1          
       
        return "" if min_window[0] == float('inf') else s[min_window[1]:min_window[2]+1]  

#Time optimization when s is greatly larger than t
#Time: O(T+S)
#Space: O(T+S)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        if s == t:
            return s
        
        lookup = Counter(t)
        #initial
        curr_window = Counter()
        #optimize time by filtering s first
        filter_s = []
        for i, ch in enumerate(s):
            if ch in lookup:
                filter_s.append((ch, i))
        
        l = 0
        r = 0
        found = 0
        min_window = (float('inf'), l, r)
        #r move to find valid window
        while r < len(filter_s):
            #move right pointer one step and check if satisfy substring
            if r < len(filter_s) and found < len(lookup):
                curr_window[filter_s[r][0]] = curr_window.get(filter_s[r][0], 0)+1
                if filter_s[r][0] in lookup and curr_window[filter_s[r][0]] == lookup[filter_s[r][0]]:
                    found +=1
                
            #print("match", curr_window, found, lookup)    
            
            #once we found, move left pointer as much as we can until it's not match the requirement
            while l < len(s) and found == len(lookup):
                start = filter_s[l][1]
                end = filter_s[r][1]
                #update min window
                if min_window[0] > end-start+1:
                    min_window = (end-start+1, start, end)
                curr_window[filter_s[l][0]] -=1
                if filter_s[l][0] in lookup and curr_window[filter_s[l][0]] < lookup[filter_s[l][0]]:
                    found-=1
                l+=1
            #print("min window", min_window)        
            r+=1    
           
        #print(lookup)
        
       
        return "" if min_window[0] == float('inf') else s[min_window[1]:min_window[2]+1]   