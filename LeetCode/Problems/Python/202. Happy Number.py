class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getNext(n):
            temp = 0
            while n > 0:
                digit = n % 10
                temp += digit**2
                n //= 10
            return temp
        
        lookup = set()
        
        while n!=1 and n not in lookup:
            lookup.add(n)
            n = getNext(n)
           
        return n==1