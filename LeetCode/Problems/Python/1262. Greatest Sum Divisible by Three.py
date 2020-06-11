class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        seen = [0, 0, 0]
        for n in nums:
            temp = seen.copy()
            print("Round, ", n)
            print("ref", temp)
            for i in temp:
                seen[(n+i)%3] = max(seen[(n+i)%3],i+n)
                print(seen)
                
            
        return seen[0]