class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        if not tokens:
             return 0
            
        stack = []
        operator = ['+','-','*','/']
        for t in tokens:
            if t not in operator:
                stack.append(t)
            else:
                b = stack.pop()
                a = stack.pop()
                print(a + t + b)
                if t == '+':
                    stack.append(str(int(a)+int(b)))
                elif t == '-':
                    stack.append(str(int(a)-int(b)))
                elif t == '*':
                    stack.append(str(int(a)*int(b)))
                elif t == '/':
                    stack.append(str(int(float(a)/float(b))))
        return stack.pop()
                    
        