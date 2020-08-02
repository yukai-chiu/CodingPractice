#Time: O(S), S is the length of the source code
#Space: O(S)
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        if not source:
            return []
        
        parsed = []
        commented = False
        buffer = []
        for line in source:
            i = 0
            while i < len(line):
                ch = line[i]
                # Case //: move pointer to the end
                if not commented and ch == "/" and i+1 < len(line) and line[i+1] == "/":
                    i = len(line)
                    
                # Case /*: start of the comment block 
                elif not commented and ch == "/" and i+1 < len(line) and line[i+1] == "*":
                    commented = True
                    i+=1
                # Case */: close of the comment block       
                elif commented and ch == "*" and i+1 < len(line) and line[i+1] == "/":
                    commented = False
                    i+=1
                    
                elif not commented:
                    buffer.append(ch)
                i+=1        
                    
            if not commented and len(buffer) > 0:
                parsed.append("".join(buffer))
                buffer = []
                    
        return parsed