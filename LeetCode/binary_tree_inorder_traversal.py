"""
Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode):
        stack = []
        res = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.val != None:
                res.append(cur.val)
            cur = cur.right
        return res
            

# Input: [1,null,2,3]
#   1
#    \
#     2
#    /
#    3

sol = Solution()
tree = TreeNode(1)
tree.left = TreeNode(None)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)

inorder = sol.inorderTraversal(tree)
print(inorder)