#Sorted by string
#Time: O(nklogk), n is the length of strs, k is the longest string
#Space: O(n*k)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        
        #sorted string will be the same
        for s in strs:
            anagram = sorted([ch for ch in s])
            lookup[tuple(anagram)].append(s)

            
        return lookup.values()

#String representation
#Time: O(n*k)
#Space: O(n*k)        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        
        #sorted string will be the same
        for s in strs:
            anagram = [0] * 26
            for ch in s:
                anagram[ord(ch)-ord('a')] +=1
            
            #print(anagram)
            lookup[tuple(anagram)].append(s)

            
        return lookup.values()