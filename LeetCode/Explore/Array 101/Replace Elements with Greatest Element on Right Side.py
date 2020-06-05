#Time: O(n)
#Space: O(n)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #Brute force
        #new an array, initial the last as -1
        #iterate backward, always compare the arr[i+1] and result[i+1]
        if not arr:
            return arr
        result = arr.copy()
        result[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            result[i] = max(result[i+1], arr[i+1])
        return result


#In-place
#Time: O(n)
#Space: O(1)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #in-place
        #maintain the max value
        if not arr:
            return arr
        
        max_right = -1
        for i in range(len(arr)-1,-1,-1):
            #cache it for later use
            temp = max_right
            #calculate the seen maximum value
            max_right = max(max_right, arr[i])
            #set the cache value
            arr[i] = temp
        return arr
        