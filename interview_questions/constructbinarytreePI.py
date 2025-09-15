class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class solution:
    def binarytree(self,preorder,inorder):
        memory = {}
        for i,e in enumerate(inorder):
            memory[e] = i

        root = self.helper(self,preorder[::-1],inorder,0,len(inorder),memory)
        return root

    def helper(preorder,inorder,leftpointer,rightpointer,memory):
        if leftpointer >= rightpointer :
            return None

        num = preorder.pop()
        root = TreeNode(num)
        idx = memory.get(num)

        root.left = self.helper(preorder,inorder,0,idx,memory)
        root.right = self.helper(preorder,inorder,idx+1,len(inorder),memory)

        return root

        
        
        