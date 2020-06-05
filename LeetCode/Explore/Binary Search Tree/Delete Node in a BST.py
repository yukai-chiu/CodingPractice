# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#my first implementation
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        #iterative
        stack = []
        #case 1:
        #it is leaf --> directly remove it
        #case 2:
        #it has only one child --> use the child to replace the noded
        #case 3:
        #two childs -->use predecessor or successor to replace it
        
        #successor --> if the node has right child, it's the left most leaf of the right subtree
        #predecessor --> if the node has left child, it's the right most leaf of the left subtree
        
        #we can use binary search to search the node
        target = root
        parent = None
        print(target.val)
        while target:
            print(target.val)
            #search in BST
            if target.val > key:
                parent = (target,True)
                target = target.left
            elif target.val < key:
                parent = (target,False)
                target = target.right
            #when we found it
            elif target.val == key:
                print("Found")
                #case 1
                if not target.left and not target.right:
                    if target == root:
                        return None 
                    else: 
                        if parent[1]:
                            parent[0].left = None
                        else:
                            parent[0].right = None
                        return root
                #case 2
                elif not target.left or not target.right:
                    if target.left:
                        if not parent:
                            return target.left
                        if parent[1]:
                            parent[0].left = target.left
                        else:
                            parent[0].right = target.left
                        
                    elif target.right:
                        if not parent:
                            return target.right
                        else:
                            if parent[1]:
                                parent[0].left = target.right
                            else:
                                parent[0].right = target.right
                    return root
                #case 3
                elif target.left and target.right:
                    succ = target.right
                    succ_para = target
                    while succ.left:
                            succ_para = succ
                            succ = succ.left
                    print("Succ",succ,succ.left)
                    #if succ.right:
                    #    #doesn't go left
                    if succ_para == target:
                        target.right = succ.right
                        target.val = succ.val

                    else:
                        target.val = succ.val
                        succ_para.left = succ.right

                    #else:
                    #    target.val = succ.val
                    #    succ_para.left = None
                    return root
        return root
                            
                            
                        
                    
#iterative
#Time: O(h) = O(logn)
#Space: O(1)
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        
        #case 1:
        #it is leaf --> directly remove it
        #case 2:
        #it has only one child --> use the child to replace the noded
        #case 3:
        #two childs -->use predecessor or successor to replace it
        
        #successor --> if the node has right child, it's the left most leaf of the right subtree
        #predecessor --> if the node has left child, it's the right most leaf of the left subtree
        
        #we can use binary search to search the node
        target = root
        parent = None
        left_child = True
        while target:
            #search in BST
            if target.val > key:
                parent = target
                left_child = True
                target = target.left
            elif target.val < key:
                parent = target
                left_child = False
                target = target.right
                
            #when we found it
            elif target.val == key:
                #case 1
                if not target.left and not target.right:
                    #if the target is the root
                    if not parent:
                        root = None
                        
                    #otherwise we check whether it is the left or right child of it's parent
                    else: 
                        if left_child:
                            parent.left = None
                        else:
                            parent.right = None
                    return root
                
                #case 2
                elif not target.left:
                    #replace the root with right child
                    if not parent:
                        return target.right
                    else:
                        if left_child:
                            parent.left = target.right
                        else:
                            parent.right = target.right
                    return root 
                    
                elif not target.right:
                     #replace the root with left child
                    if not parent:
                        return target.left
                    else:
                        if left_child:
                            
                            parent.left = target.left
                        else:
                            parent.right = target.left
                    return root        
 
                        
                #case 3
                elif target.left and target.right:
                
                    #we need to find the inorder successor, this is the smallest node that is larger than target
                    #replace the target with it's value and delete the successor
                    succ = target.right
                    succ_para = target
                    while succ.left:
                            succ_para = succ
                            succ = succ.left
                    #case 3-1: the right node of target is the successor,
                    #which means it doesn't have left child, we can set the target.right = succ.right, it'll handle the None case
                    if succ_para == target:
                        target.right = succ.right
                        target.val = succ.val
                    
                    #if it actually goes down the tree
                    else:
                        #replace with the value
                        target.val = succ.val
                        #set the parent.left to succ.right, since it won't have any left child, this will also handle the None case
                        succ_para.left = succ.right

                    return root 
        return root