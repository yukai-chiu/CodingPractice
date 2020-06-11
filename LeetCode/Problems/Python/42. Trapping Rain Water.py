#Brute force method
#Time: O(n^2)
#Space: O(1)
#Time limit exceeded
class Solution:
    def trap(self, height: List[int]) -> int:        
        if not height:
            return 0
        ans = 0
        for i in range(0, len(height)):
            l = i-1
            r = i+1
            l_max = height[i]
            r_max = height[i]
            while l >=0:
                if height[l] > l_max:
                    l_max = height[l]
                l-=1
            while r < len(height):
                if height[r] > r_max:
                    r_max = height[r]
                r+=1
            #print(i, l_max, r_max)
            ans += (min(l_max, r_max) - height[i])
            #print(ans)
        return ans
            

#Dynamic Programming
#Time: O(n)
#Space: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:        
        if not height:
            return 0
        ans = 0
        dp = [0] * len(height)
        left_max = height[0]
        right_max = height[-1]
        for i in range(len(height)):
            if height[i] > left_max:
                left_max = height[i]
            dp[i] = left_max
        for i in range(len(height)-1,-1,-1):
            if height[i] > right_max:
                right_max = height[i]
            dp[i] = min(dp[i],right_max)
        
        for i in range(len(height)):
            ans += dp[i] - height[i]
                
        return ans
            
#Two pointer
#optimzation from DP
#Time: O(n)
#Space: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:        
        if not height:
            return 0
        ans = 0
        l = 0
        r = len(height)-1
        l_max = height[0]
        r_max = height[-1]
        while (l<r):
            while l < r and l_max <= r_max:
                ans += l_max - height[l]
                l+=1
                l_max = max(height[l], l_max)
            while l < r and l_max > r_max:
                ans += r_max - height[r]
                r-=1
                r_max = max(height[r],r_max)
            
        return ans


#Stack
#Different concept
#Time: O(n)
#Space: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:        
        if not height:
            return 0
        i = 0
        stack = []
        ans = 0
        while (i<len(height)):
            while stack and height[i] > height[stack[-1]]:
                curr = stack.pop()
                if stack:
                    diff = min(height[stack[-1]],height[i]) - height[curr]
                    ans += (diff * (i-stack[-1]-1))
            stack.append(i)
            i+=1
        return ans
            
            