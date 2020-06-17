class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        
        for col in range(len(text2)-1, -1, -1):
            for row in range(len(text1)-1, -1, -1):
                if text2[col] == text1[row]:
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row+1][col], dp[row][col+1])
        #print(dp)
                
        return dp[0][0]