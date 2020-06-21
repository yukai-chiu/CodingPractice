#baccktracking
#Time: O(3^m*4^n)
#Space: O(3^m*4^n)
class Solution:
    def letterCombination(self, digits, dict, result, curr):
        if not digits:
            result.append(curr)
            return
        
        for ch in dict[digits[0]]:
            self.letterCombination(digits[1:], dict, result, curr+ch)
        
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dict =  {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}


        result = []
        self.letterCombination(digits, dict, result, "")
       
        return result