class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        anagram = Counter(s1)

        window = Counter()
        start = 0
        result = []
        idx = 0
        while idx < len(s2):
            if s2[idx] in anagram:
                window[s2[idx]]+=1
                #move left ptr
                while window[s2[idx]] > anagram[s2[idx]]:
                    window[s2[start]]-=1
                    start+=1
                    
                if window == anagram:
                    return True

            else:
                #reset
                window = Counter()
                start = idx+1
            idx+=1
            
        return False