#hash map
#Time: O(n)
#Space: O(1), since O(26) is the maximum
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        lookup = {}
        for index, char in enumerate(s):
            lookup[char] = lookup.get(char, []) +[index]
        for key, value in lookup.items():
            if len(value) == 1:
                return value[0]
        #print(lookup)
    
        return -1


#Cleaner solution using counter
#Time: O(n)
#Space: O(1)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        lookup = Counter(s)
        for index, char in enumerate(s):
            if lookup[char] == 1:
                return index
        return -1