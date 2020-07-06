#recursion + memo
#Time: O(m*n)
#Space: O(m*n)
class Solution:
    def min_distance(self, word1, word2, memo):
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        
        if (word1, word2) in memo:
            return memo[(word1, word2)]
        
        if word1[0] == word2[0]:
            dist = self.min_distance(word1[1:], word2[1:], memo)
        elif word1[0] != word2[0]:
            #delete, insert
            dist = min(self.min_distance(word1[1:], word2, memo), self.min_distance(word1, word2[1:], memo))+1
            #replace
            dist = min(dist, self.min_distance(word1[1:], word2[1:], memo)+1)
        
        memo[(word1, word2)] = dist
        return memo[(word1, word2)]
            
        
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        
        return self.min_distance(word1, word2, {})

#dynamic programming
#Time: O(m*n)
#Space: O(m*n)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
                
        
            
        for i in range(1,len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1

        return dp[-1][-1]