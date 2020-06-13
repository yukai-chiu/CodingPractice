#sorting 
#Time: O(nlogn)
#Space: O(n)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        w = Counter(words)     
        #reverse
        w = [(-value,key) for key, value in w.items()]
        w.sort()
        #only pick the top k items
        return [w[i][1] for i in range(k)]

#Heap
#Time: O(n + klogn), n for heapify, klogn for heappop
#Space: O(n)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        w = Counter(words)
       
        heap = [(-value,key) for key, value in w.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for i in range(k)]
                