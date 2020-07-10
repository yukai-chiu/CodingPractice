#Time: O(n)
#Space: O(n)
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        lookup = Counter()
        prefix = 0
        result = 0
        lookup[0]+=1
        for i, a in enumerate(A):
            prefix+=a
            remain = prefix % K
            if remain in lookup:
                result+= lookup[remain]
            
            lookup[remain]+=1
        
        return result