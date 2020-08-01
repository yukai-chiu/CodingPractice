class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
             return []
            
        last = {s:i for i, s in enumerate(S)}
        
        start = 0
        end = 0
        partition = []
        for i,s in enumerate(S):
            end = max(end, last[s])
            if i==end:
                partition.append(end-start+1)
                start = end+1
        return partition