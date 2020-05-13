class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ""
        
        #Solution 1: Horizontal Scan
        prefix = strs[0]
        for i in range(len(strs)):
            while prefix != strs[i][0:len(prefix)]:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix

        #Solution 2: Vertical Scan
        