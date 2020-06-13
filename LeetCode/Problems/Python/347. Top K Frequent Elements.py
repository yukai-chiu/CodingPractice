#Heap
#Time: O(n+klogn)
#Space: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = Counter(nums)
        n = [(-value, key) for key,value in n.items()]
        heapq.heapify(n)
        return [heapq.heappop(n)[1] for _ in range(k)]