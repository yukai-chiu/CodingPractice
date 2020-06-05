
#Loop and Flip
#Time: O(1)
#Space: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        if not n:
            return 0

        return bin(n).count('1')


class Solution:
    def hammingWeight(self, n: int) -> int:
        if not n:
            return 0

        ans = 0
        for i in range(31,-1,-1):
            bit = (n >> i) & 1 
            if bit:
                ans+=1

        return ans

#Bit Manipulation Trick
#Time: O(1)
#Space: O(1)
#but faster than the pervious method since it ends at the bits size of n, wors case is 32 nits
class Solution:
    def hammingWeight(self, n: int) -> int:
        if not n:
            return 0

        ans = 0
        while n != 0:
            n &= n - 1
            ans+=1
     
        return ans


class Solution:
    def countBits(self, num: int) -> List[int]:

        dp = [0] * (num+1)
        
        for i in range(1, num+1):
            dp[i] = dp[i&(i-1)] + 1
        return dp