class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        i = 0
        parsed = []
        l = 0
        r = len(s)-1
        
        while l < len(s)-1 and s[l] == " ":
            l+=1
        while r >= 0 and s[r] == " ":
            r-=1
            
        words = s[l:r+1].split(" ")
        print(words)
        for i in range(len(words)-1,-1,-1):
            if words[i] != "":
                parsed.append(words[i])
        
        
        return " ".join(parsed)
            