class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ""
        
        #Solution 1: Horizontal Scanning
        prefix = strs[0]
        for i in range(len(strs)):
            while prefix != strs[i][0:len(prefix)]:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix

        #Solution 2: Vertical Scanning
        for i,c in enumerate(strs[0]):
            for s in strs[1:]:
                if i == len(s) or c != s[i]:
                    return strs[0][:i]
        return strs[0]
        