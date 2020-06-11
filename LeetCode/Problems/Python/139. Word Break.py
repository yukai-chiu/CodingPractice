class Solution:  
    def word_break(self, n,start, wordDict, memo):
        if n[start:] in wordDict:
            return True
        
        if start in memo:
            return memo[start]

        for i in range(len(n[start:])):
            #print(n[start:start+i+1], n[start+i+1:])
            if n[start:start+i+1] in wordDict:
                if n[:start+i+1] not in wordDict:
                    wordDict.append(n[:start+i+1])
                
                if self.word_break(n,start+i+1, wordDict, memo):
                    memo[start] = True
                    return memo[start]
        
        memo[start] = False
        return memo[start]
        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False
        
        
        memo = {}
        return self.word_break(s,0, wordDict, memo)




#iterative
class Solution:  
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False
        
        word_dict = set(wordDict)
        
        visited = [0] * len(s)
        queue = [0]
        while queue:
            curr = queue.pop(0)
            #we want to use memoization
            #if we haven't traverse from it
            if visited[curr] == 0:
                for i in range(curr,len(s)):
                    if s[curr:i+1] in word_dict:
                        queue.append(i+1)
                        if i+1 == len(s):
                            return True
                visited[curr] = 1

        return False