class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeros = 0
        for i in range(n):
            if i + zeros > len(arr)-1:
                
                break
            if arr[i] == 0:
                if i + zeros == len(arr)-1:
                    arr[n-1] = 0
                    n-=1
                    break
                zeros += 1
                
        last = n - zeros - 1

        for j in range(last, -1, -1):
            if arr[j] == 0:
                arr[j + zeros] = 0
                zeros -= 1
                arr[j + zeros] = 0
            else:
                arr[j + zeros] = arr[j]

                
            