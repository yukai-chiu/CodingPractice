class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        if a == '0' and b == '0':
            return '0'
        carry = 0 
        result = ""
        if len(a) >len(b):
            for i in range(1, len(a)+1, 1):
                
                if len(b) - i >= 0:
                    if b[-i] == '1' and a[-i] == '1':
                        curr = '0'
                        if carry == 1:
                            curr = '1'
                        carry = 1
                    
                        
                    elif b[-i] == '1' or a[-i] == '1':
                        curr = '1'
                        if carry == 1:
                            curr = '0'
                            carry = 1
                    else:
                        if carry == 1:
                            curr = '1'
                            carry = 0
                        else:
                            curr = a[-i]
                      
                else:
                    if carry == 1 and a[-i] == '1':
                        curr = '0'
                        carry = 1
                    elif carry == 1:
                        curr = '1'
                        carry = 0
                    else:
                        curr = a[-i]
                result = curr + result
                    
            if carry == 1:
                
                result = "1" + result
                carry = 0
            return result
        else:
            for i in range(1, len(b)+1, 1):
                if len(a) - i >= 0:
                    if b[-i] == '1' and a[-i] == '1':
                        curr = '0'
                        if carry == 1:
                            curr = '1'
                        carry = 1
                        
                    elif b[-i] == '1' or a[-i] == '1':
                        curr = '1'
                        if carry == 1:
                            curr = '0'
                            carry = 1
                    else:
                        if carry == 1:
                            curr = '1'
                            carry = 0
                        else:
                            curr = b[-i]
                else:
                    if carry == 1 and b[-i] == '1':
                        curr = '0'
                        carry = 1
                    elif carry == 1:
                        curr = '1'
                        carry = 0
                    else:
                        curr = b[-i]
                result = curr + result
                    
            if carry == 1:
                
                result = "1" + result
                carry = 0
            return result
                    

            