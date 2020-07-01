#Time: O(C), C is the length of all the words
#Space: O(1), because order bounded by 26
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if not words or not order:
            return False
        
        aliendict = {}
        for idx, ch in enumerate(order):
            aliendict[ch] = idx
            
        #extract relationship
        for w1, w2 in zip(words, words[1:]):
            for ch in range(min(len(w1), len(w2))):
                if w1[ch] != w2[ch]:
                    if aliendict[w1[ch]] > aliendict[w2[ch]]:
                        return False
                    break
            else:
                if len(w2) < len(w1):
                    return False
        
        return True