#hash map
#Time: O(n)
#Space: O(k)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        #first try
        #counter 
        if not s:
            return 0
   
        longest = 0
        counter = Counter()
        start = 0
        for i, c in enumerate(s):
            counter[c]+=1
            while len(counter) > k:
                counter[s[start]]-=1
                if counter[s[start]] ==0:
                    del counter[s[start]]
                start+=1
            longest = max(longest, i-start+1)
        return longest

#hash map
#Time: O(n)
#Space: O(k)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        window = Counter()
        t = 0
        l = 0
        r = 0
        
        while r < len(s):
            window[s[r]]+=1
            #print(t)
            if len(window) <= k:
                if r-l+1 > t:
                    t = r-l+1
            #move left bound of the window
            while len(window) > k:
                window[s[l]]-=1
                if window[s[l]] == 0:
                    del window[s[l]]
                l+=1
            r+=1

        return t