#Time: O(nlogn)
#Space: O(n)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if not logs:
            return []
        
        def formedKey(log):
            log_type, data = log.split(" ", 1)
            if data[0].isalpha():
                return (0, data, log_type)
            else:
                return (1,)
        logs.sort(key = formedKey)    
        return logs