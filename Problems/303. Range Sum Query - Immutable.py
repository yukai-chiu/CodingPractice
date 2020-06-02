class NumArray:

    def __init__(self, nums: List[int]):
        self.sum_range = [0] * len(nums)
        
        if len(nums) > 0:
            self.sum_range[0] = nums[0]
            for i in range(1, len(nums)):
                self.sum_range[i] = self.sum_range[i-1]+nums[i]
        
        

    def sumRange(self, i: int, j: int) -> int:
        if i<0 or j > len(self.sum_range):
            return 0
        
        if i > 0:
            return self.sum_range[j] - self.sum_range[i-1]
        elif i ==0:
            return self.sum_range[j]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)