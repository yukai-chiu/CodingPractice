#BFS
#Time: O(M^2*N)
#Space: O(M^2*N)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        
        graph = defaultdict(set)
        
        #for loop M*N, create new string M => O(M^2*N)
        for w in wordList:
            for i in range(len(w)):
                graph[w[:i]+"*"+w[i+1:]].add(w)
   

        queue = deque()
        queue.append([beginWord,1])
        visited = set([beginWord])
        
        #worst case also O(M^2*N)
        while queue:
            word, steps = queue.popleft()
            for i in range(len(word)):
                for node in graph[word[:i]+"*"+word[i+1:]]:
                    if node not in visited:
                        visited.add(node)
                        if node == endWord:
                            return steps+1
                        queue.append([node, steps+1])
                 
        return 0
        