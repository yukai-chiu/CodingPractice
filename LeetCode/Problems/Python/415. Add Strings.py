class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        M = len(num1)
        N = len(num2)
        
        ptr1 = M-1
        ptr2 = N-1
        carry = 0
        result = deque()
        while ptr1 >=0 and ptr2 >=0:
            n1 = ord(num1[ptr1]) - ord('0')
            n2 = ord(num2[ptr2]) - ord('0')
            digit = n1 + n2 + carry
            carry = digit // 10
            digit = digit % 10
            result.appendleft(chr(ord('0')+digit))
            ptr1-=1
            ptr2-=1
        
        
        while ptr1 >=0:
            n1 = ord(num1[ptr1]) - ord('0')
            digit = n1 + carry
            carry = digit // 10
            digit = digit % 10
            result.appendleft(chr(ord('0')+digit))
            ptr1-=1
            
        while ptr2 >=0:
            n2 = ord(num2[ptr2]) - ord('0')
            digit = n2 + carry
            carry = digit // 10
            digit = digit % 10
            result.appendleft(chr(ord('0')+digit))
            ptr2-=1
        
        if carry !=0:
            result.appendleft('1')
        return "".join(result)