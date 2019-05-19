class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.rigth = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")

    def preorder_print(self, start, traversal):
        """Root->Left->Rigth"""
        if start:
            traversal += (str(start.value) + " - ")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.rigth, traversal)
        return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.rigth = Node(3)
tree.root.left.left = Node(4)
tree.root.left.rigth = Node(5)
tree.root.rigth.left = Node(6)
tree.root.rigth.rigth = Node(7)
tree.root.rigth.rigth.rigth = Node(8)

x = tree.print_tree("preorder")
print(x)
