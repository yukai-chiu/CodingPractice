#DP
#Time: O(n^2)
#Space: O(n)
class Solution:
    def numTrees(self, n: int) -> int:
        
        if n <2:
            return n
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        
        #G(n): the number of unique BST for a sequence of length n
        #F(i,n): the number of unique BST, where i is the root of it(1<=i<=n)
        #G(n) = Sum[1,n]F(i,n)
        #we are calculating all the unique BST with all kind of roots
        #
        #Let's see F(i,n)
        #it's left subtree will be G(i-1),
        #right subtree will be G(n-i)
        #so F(i,n) = G(i-1) * G(n-i)
        #therefore we can get:
        #G(n) = Sum[1,n]G(i-1) * G(n-i)
        
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1]*dp[i-j]
        #print(dp)
        return dp[n]