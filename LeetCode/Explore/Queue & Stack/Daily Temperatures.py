class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return 0
        
        stack = []
        result = [0] * len(T)
        for i in range(len(T)-1, -1, -1):
            #pop until the first warmer day,
            #will pop out all the colder one. 
            #for days ealier, they will be bounded by the current i so we don't need those colder days
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                result[i] = stack[-1] - i
            stack.append(i)   
        return result