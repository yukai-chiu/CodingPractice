class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        #two pointer: one start from front and one from end
        #odd pointer from front, even from end
        #swap and step
        if not A or len(A) == 1:
            return A

        odd = 0
        even = len(A) - 1
        while odd < even:
            #if couldn't find one, it will exit this while loop with odd = even
            while odd < even and A[odd] % 2 == 0:
                odd+=1
            while odd < even and A[even] % 2 == 1:
                even-=1
            #if odd = even, it's okay to swap again, can handle it
            A[odd], A[even] = A[even], A[odd]

        return A