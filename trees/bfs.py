class Node :
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Binarytree():
    def __init__(self,value):
        self.root = Node(value)

    def bfs(self):
        if not self.root:
            return

        queue = [self.root]
        while queue:
            node = queue.pop(0)   # Remove the first element
            print(node.value, end=" ")

            if node.left:         # Add left child to queue
                queue.append(node.left)

            if node.right:        # Add right child to queue
                queue.append(node.right)


tree = Binarytree(3)

tree.root.left = Node(4)
tree.root.left.left = Node(6)
tree.root.left.right = Node(7)

tree.root.right = Node(5)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

tree.bfs()