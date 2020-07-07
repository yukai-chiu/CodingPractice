#Time: O(n)
#Space: O(n)
class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return "/"
        
        result = []
        
        for p in path.split('/'):
            if p == '..':
                if result:
                    result.pop()
            elif p == '.' or p == '':
                continue
            else:
                result.append(p)

        return '/' + '/'.join(result)