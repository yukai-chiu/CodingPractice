class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        if not products:
            return []
        products.sort()
        
        suggested = []
        for i in range(len(searchWord)):
            prefix = searchWord[:i+1]
            lo = 0
            hi = len(products)
            temp = []
            while lo < hi:
                mid = lo +(hi-lo)//2
                if prefix <= products[mid]:
                    hi = mid
                else:
                    lo = mid+1
            for j in range(3):
                if lo+j < len(products) and prefix in products[lo+j]:
                    temp.append(products[lo+j])
            suggested.append(temp)
        return suggested