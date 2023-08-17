# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorderTraversal(root):
    if root is None:
        return []

    left_subtree = inorderTraversal(root.left)
    current = [root.val]
    right_subtree = inorderTraversal(root.right)

    return left_subtree + current + right_subtree
