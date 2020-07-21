class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        
        in_map = dict([(x,i) for i, x in enumerate(inorder)])
        
        head = TreeNode(preorder[0])
        stack = [head]
        for i, x in enumerate(preorder[1:]):
            node = TreeNode(x)
            if in_map[x] < in_map[stack[-1].val]:
                stack[-1].left = node
            else:
                while stack and in_map[x] > in_map[stack[-1].val]:
                    parent = stack.pop()
                parent.right = node
            stack.append(node)
        
        return head