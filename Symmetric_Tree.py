# https://leetcode.com/problems/symmetric-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root):
    if root is None:
        return True
    child01 = isSymmetric(root.left)
    child02 = isSymmetric(root.right
                          
    if child01 == child02:
        return True

    return False


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(2)
    tree.left.left = None
    tree.right.left = None
    tree.left.right = 3
    tree.right.right = 3

    print(isSymmetric(tree))
