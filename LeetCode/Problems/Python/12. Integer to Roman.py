class Solution:
    def intToRoman(self, num: int) -> str:
        if not num:
            return ""
        roman = []
        lookup = [("M",1000),("CM", 900),("D", 500),("CD", 400),("C", 100),("XC", 90),("L", 50),("XL", 40),("X", 10),('IX', 9),('V', 5),('IV', 4),('I', 1)]
        
        for symbol, val in lookup:
            count, num = divmod(num, val)
            roman.append(symbol*count)
        return "".join(roman)

class Solution:
    def intToRoman(self, num: int) -> str:
        if not num:
            return ""
        roman = deque()
        lookup = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        idx = 0
        while num:
            digit = num % 10
            print(digit, lookup[idx])
            if digit == 5:
                roman.appendleft(lookup[idx+1])
            elif digit == 4:
                roman.appendleft(lookup[idx+1])
                roman.appendleft(lookup[idx])
            elif digit == 9:
                roman.appendleft(lookup[idx+2])
                roman.appendleft(lookup[idx])
            elif digit >5:
                roman.appendleft(lookup[idx]*(digit-5))
                roman.appendleft(lookup[idx+1])
            elif digit <4:
                roman.appendleft(lookup[idx]*digit)
                    
            num//=10
            idx+=2
        return "".join(roman)