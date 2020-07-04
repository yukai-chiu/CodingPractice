#Time: O(s+p)
#Space: O(1) since 26 characters can be seen as constant
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagram = Counter(p)

        window = Counter()
        start = 0
        result = []
        idx = 0
        while idx < len(s):
            if s[idx] in anagram:
                window[s[idx]]+=1
                #move left ptr
                while window[s[idx]] > anagram[s[idx]]:
                    window[s[start]]-=1
                    start+=1
                    
                if window == anagram:
                    result.append(start)

            else:
                #reset
                window = Counter()
                start = idx+1
            idx+=1
            
        return result