#Time: O(n)
#Space: O(1), 26 characters in total
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        
        count = list(Counter(tasks).values())
        time = 0
        count.sort()
        max_task =count.pop()
        max_idle = (max_task-1) * n
        while count and max_idle > 0:
            max_idle-= min(max_task-1, count.pop())
            
        max_idle = max(0, max_idle)
        return max_idle + len(tasks)
                