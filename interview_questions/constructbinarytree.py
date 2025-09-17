class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstfrompreorder(self,preorder):
        root = TreeNode(preorder[0])
        stack = [root]
        for i in range(1,len(preorder)):
            if stack[-1].val > preorder[i]:
                node = TreeNode(preorder[i])
                stack[-1].left = node
                stack.append(node)
            else:
                while stack and stack[-1].val < preorder[i]:
                    pop = stack.pop()
                    node = TreeNode(preorder[i])
                    pop.right = node
                    stack.append(node)

        return root
       