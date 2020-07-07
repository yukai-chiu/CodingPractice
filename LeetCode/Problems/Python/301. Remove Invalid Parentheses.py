#my first implementation, DFS + memo
#Time: O(2^s)
#Space: O (s)
class Solution:
    def remove(self, s, form, count, curr, ans, memo):
        if not s:
            if form == 0:
                if count < ans[0]:
                    ans[0] = count
                    ans[1] = set()
                    ans[1].add(tuple(curr))
                elif count == ans[0]:
                    ans[1].add(tuple(curr))
            return 
        #early termination
        if count > ans[0]:
            return
        #memo
        if (s, tuple(curr)) in memo:
            return
        
        ch = s[0]
        if ch.isalnum():
            self.remove(s[1:], form, count, curr + [ch], ans, memo)

        elif ch == ')':
            if form == 0:
                #remove it
                self.remove(s[1:], form, count+1, curr, ans, memo)
            elif form > 0:
                #keep it
                self.remove(s[1:], form-1, count, curr + [ch], ans, memo)
                #remove it
                self.remove(s[1:], form, count+1, curr, ans, memo)


        elif ch == '(':
            self.remove(s[1:], form+1, count, curr + [ch], ans, memo)
            self.remove(s[1:], form, count+1, curr, ans, memo)
        
        memo[(s, tuple(curr))] = True
        
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return [""]
        
        ans = [float('inf'),set()]
        
        self.remove(s, 0, 0, [], ans, {})

        return ["".join(x) for x in ans[1]]