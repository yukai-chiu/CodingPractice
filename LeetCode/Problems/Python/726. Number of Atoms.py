#Stack
#Time: O(n^2)
#Space: O(n)
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        if not formula:
            return ""
        count= Counter()
        #our result counter
        stack = [count]
        result = []
        N = len(formula)
        i = 0
        while i < N:
            if formula[i] == '(':
                stack.append(Counter())
                i+=1
            elif formula[i] == ')':
                top = stack.pop()
                i+=1
                #we need to find the number following parenthesis
                start = i
                while i<N and formula[i].isdigit():
                    i+=1
                
                m = int(formula[start:i] or 1)
                
                for key, value in top.items():
                    stack[-1][key] += value * m
            #handle upper and lower
            else:
                #we should start from upper case
                start = i
                i+=1
                #check the following lower case
                while i < N and formula[i].islower():
                    i+=1
                element = formula[start:i]
                #check digit
                start = i
                while i<N and formula[i].isdigit():
                    i+=1
                m = int(formula[start:i] or 1)
                stack[-1][element] += m
         
        print(sorted(stack[-1]))
        
        for key in sorted(stack[-1]):
            result.append(key)
            #print()
            if stack[-1][key] > 1:
                result.append(str(stack[-1][key]))
            
        return "".join(result)
            
       
        
        