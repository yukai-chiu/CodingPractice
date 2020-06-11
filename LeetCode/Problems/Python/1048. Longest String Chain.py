class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        
        #setup a hashmap for dp
        #Original sort code O(nlogn): words = sorted(words, key=len)
        #Since we know the range of the length of the word, we can optimize it using bucket sort
        #Optimized the sort to O(n)
        bucket = [[] for _ in range(16)]
        for w in words:
            bucket[len(w)-1].append(w)           
        words = []
        for b in bucket:
            if b:
                words +=b    

        hash_map = collections.Counter(words)
     
        #from backward, remove a character and see if there's a match
        #if match a target, we can set hash[target] = max(hash[target], hash[curr] + 1)
        for i in range(len(words) -1 , -1, -1):
            for j in range(len(words[i])):
                if words[i][:j] + words[i][j+1:] in hash_map:
                    hash_map[words[i][:j] + words[i][j+1:]] = max(hash_map[words[i][:j] + words[i][j+1:]], hash_map[words[i]] +1)
        
        return max(hash_map.values())