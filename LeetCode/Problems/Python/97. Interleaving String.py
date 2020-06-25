#DP
#Time: O(m*n)
#Space: O(m*n)
class Solution:    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #first thought: find if s1 and s2 are substring?\
        if len(s3) != len(s1) +len(s2):
            return False
        dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]

        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i ==0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and (s2[j-1] == s3[i+j-1])
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and (s1[i-1] == s3[i+j-1])
                else:
                    dp[i][j] = (dp[i-1][j] and (s1[i-1] == s3[i+j-1])) or dp[i][j-1] and (s2[j-1] == s3[i+j-1])

        return dp[-1][-1]
                    
        


#brute force
#Time limit exceeded
#Time: O(2^(m+n))
#Space: O(m+n)
class Solution:
    def is_interleave(self, s1, s2, s3, p1, p2, cur) -> bool:
        if cur == s3 and p1 == len(s1) and p2 == len(s2):
                return True
        ret = False

        if p1 < len(s1):
            ret = ret or self.is_interleave(s1, s2, s3, p1+1, p2, cur+s1[p1])
        if p2 < len(s2):
            ret = ret or self.is_interleave(s1, s2, s3, p1, p2+1, cur+s2[p2])
        return ret
        
        
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #first thought: find if s1 and s2 are substring?\
        if not s1 and not s2 and not s3:
            return True

        return self.is_interleave(s1, s2, s3, 0, 0, "")