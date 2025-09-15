class TreeNode:
    def__init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class solution:
    def invertbinarytree(self,root):
         if root is None:
            return

        root.left,root.right = root.right,root.left
        self.invertbinarytree(left)
        self.invertbinarytree(right)

        return root
