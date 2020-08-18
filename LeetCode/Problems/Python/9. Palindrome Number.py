#Time: O(logn)
#Space: O(logn)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x > 0):
            return False
        
        
        rev_num = 0
        while rev_num < x:
            rev_num*=10
            rev_num += x%10
            x //=10
        
        return x == rev_num or rev_num//10 == x 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        num = []

        while x:
            num.append(x%10)
            x //=10

        return num == num[::-1]