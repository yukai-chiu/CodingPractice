#recursive
#Time: O(n)
#Space: O(n)
class Solution:
    def constructPath(self, node, path, paths):
        if node:
            path += (str(node.val))

            if not node.left and not node.right:
                paths.append(path)
            else:
                path += "->"
                self.constructPath(node.left, path, paths)
                self.constructPath(node.right, path, paths)
           
        
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        paths = []
        self.constructPath(root,"", paths)
        return paths

#DFS + Stack
#Time: O(n)
#Space: O(n)
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        paths = []
        stack = [(root,"")]
        #bfs and queue for iterative
        while stack:
            curr, p = stack.pop()
            if curr:
                p += str(curr.val)
                if not curr.left and not curr.right:
                    paths.append(p)
                else:
                    p+="->"
                    stack.append((curr.left,p))
                    stack.append((curr.right,p))
            
        return paths

#BFS + Queue
#Time: O(n)
#Space: O(n)
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        paths = []
        queue = [(root,"")]
        #bfs and queue for iterative
        while queue:
            curr, p = queue.pop(0)
            if curr:
                p += str(curr.val)
                if not curr.left and not curr.right:
                    paths.append(p)
                else:
                    p+="->"
                    queue.append((curr.left,p))
                    queue.append((curr.right,p))
            
        return paths
    