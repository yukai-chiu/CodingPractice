class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack)):
            c = haystack[i]
            n = 0
            if c == needle[n]:
                while c == needle[n] and n < len(needle):
                    n+=1
                    if n >= len(needle):
                        return i
                    
                    if i+n >= len(haystack):
                        return -1
                    else:
                        c = haystack[i+n]

        return -1