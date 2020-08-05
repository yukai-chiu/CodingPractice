class Solution:
    def checkDecodings(self, s, idx, memo):
        if idx == len(s):
            return 1
        if s[idx] == '0':
            return 0
        if idx in memo:
            return memo[idx]
        
        count = 0
        #take 1
        count+= self.checkDecodings(s, idx+1, memo)
        #can take 2
        if idx+1 < len(s) and int(s[idx:idx+2])<=26:
            count+= self.checkDecodings(s, idx+2, memo)
        memo[idx] = count
        return memo[idx] 
    
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0
        
        return self.checkDecodings(s, 0, {})

class Solution:
    def countDecode(self, s, i, memo):
        if i == len(s):
            return 1
        count = 0
        if i in memo:
            return memo[i]
        if s[i] == '0':
            return count
        else:
            count = self.countDecode(s, i+1, memo)
            if i+1 < len(s) and int(s[i:i+2]) <= 26:
                count += self.countDecode(s, i+2,memo)
        memo[i] = count
        return memo[i]
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0
       
        return self.countDecode(s, 0, {})