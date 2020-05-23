#Pop Count
#use the same method of problem 191
#Time: O(n*k), k is the largest bits of the numbers
#Space: O(n), ans use n items, if we ignores the return data's space, it's O(1)
class Solution:
    def count_bits(self, n):
        bits = 0
        while n != 0 :
            n &= n-1
            bits+=1
        return bits
    
    def countBits(self, num: int) -> List[int]:
    
        ans = []
        for i in range(num+1):
            ans.append(self.count_bits(i))
        return ans


#Dynamic programming + Most Significant Bit 
#Time: O(n) 
#Space: O(n), ans use n items, if we ignores the return data's space, it's O(1)
class Solution:
    def countBits(self, num: int) -> List[int]:

        i = 0
        offset = 1
        dp = [0] * (num+1)
        
        while offset <= num:
            while i < offset and i + offset <= num:
                dp[i+offset] = dp[i] + 1
                i+=1
            offset <<= 1
            
            i = 0

        return dp


#DP + optimization of methods from problem 191, bit operations on the least significant 1-bit
#Time: O(n)
#Space: O(n), ans use n items, if we ignores the return data's space, it's O(1)
class Solution:
    def countBits(self, num: int) -> List[int]:

        dp = [0] * (num+1)
        
        for i in range(1, num+1):
            dp[i] = dp[i&(i-1)] + 1
        return dp