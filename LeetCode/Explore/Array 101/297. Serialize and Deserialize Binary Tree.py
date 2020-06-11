#BFS + Queue
#Time: O(n)
#Space: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue = collections.deque()
        queue.append(root)
        string = []
        while queue:
            node = queue.popleft()
            if not node:
                string.append('None')
                continue
            string.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        
        return ','.join(string)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        ls = data.split(',')
        
        root = TreeNode(ls[0])
        queue = collections.deque()
        queue.append(root)
        
        i = 1
        while queue and i < len(ls):
            node = queue.popleft()
            if ls[i] != 'None':
                left = TreeNode(ls[i])
                node.left = left
                queue.append(left)
            i+=1
            if ls[i] != 'None':
                right = TreeNode(ls[i])
                node.right = right
                queue.append(right)
            i+=1
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))