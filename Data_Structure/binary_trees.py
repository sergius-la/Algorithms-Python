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
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")

    def preorder_print(self, start, traversal):
        """Root->Left->Rigth"""
        if start:
            traversal += (str(start.value) + " - ")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.rigth, traversal)
        return traversal
    
    def inorder_print(self, root, traversal):
        """Left->Root->Rigth"""
        if root:
            traversal = self.inorder_print(root.left, traversal)
            traversal += (str(root.value) + " - ")
            traversal = self.inorder_print(root.rigth, traversal)
        return traversal
    
    def postorder_print(self, root, traversal):
        """Left->Rigth->Root"""
        if root:
            traversal = self.postorder_print(root.left, traversal)
            traversal = self.postorder_print(root.rigth, traversal)
            traversal += (str(root.value) + " - ")
        return traversal


# Preorder:  1 - 2 - 4 - 5 - 3 - 6 - 7 - 8
# Inorder:   4 - 2 - 5 - 1 - 6 - 3 - 7 - 8
# Postorder: 4 - 5 - 2 - 6 - 8 - 7 - 3 - 1
#
#                 1
#               /   \    
#              /     \
#             2       3
#            / \     / \
#           4   5   6   7
#                        \       
#                         8

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.rigth = Node(3)
tree.root.left.left = Node(4)
tree.root.left.rigth = Node(5)
tree.root.rigth.left = Node(6)
tree.root.rigth.rigth = Node(7)
tree.root.rigth.rigth.rigth = Node(8)

preorder = tree.print_tree("preorder")
inorder = tree.print_tree("inorder")
postorder = tree.print_tree("postorder")
