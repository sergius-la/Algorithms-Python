"""
Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode):
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                if node.val != None:
                    res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

tree = TreeNode(1)
tree.left = TreeNode(None)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)

sol = Solution()
print(sol.preorderTraversal(tree)) # [1, 2, 3]