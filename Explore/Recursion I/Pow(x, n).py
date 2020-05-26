#Brute force
#Time: O(n)
#Space: O(1)
#Time Limit Exceed
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 0:
            return 1
        
        if n < 0:
            x = 1/x
            n *= -1
        ans = 1.0
        for i in range(n):
            ans *=x
        return ans


#Fast Power Algorithm Iterative
#Time: O(logn)
#Space: O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 0:
            return 1
        
        if n < 0:
            x = 1/x
            n *= -1
        ans = 1
        product = x

        while n > 0:
            if n % 2 == 1:
                ans = ans * product
            product *= product
            n //= 2
            
         
        return ans