#Time: O(n*x), x is the average length of paths
#Space: O(n*x)
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        if not paths:
            return []
        
        files = defaultdict(list)
        
        for path in paths:
            path, f = path.split(" ", 1)
            data = f.split(" ")
            for d in data:
                name, content = d.split("(", 1)
                files[content[:-1]].append(path+"/"+name)
        result = []
        for _, f in files.items():
            if len(f) > 1:
                result.append(f)
        return result