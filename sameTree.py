# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    # If both nodes are None, they are identical
    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    if p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    return False

if __name__ == '__main__':
    node1 = TreeNode(10)
    node1.left = TreeNode(20)
    node1.right = TreeNode(30)
    node1.right.left = TreeNode(25)

    node2 = TreeNode(10)
    node2.left = TreeNode(20)
    node2.right = TreeNode(30)
    node2.right.left = TreeNode(26)

    print(isSameTree(node1,node2))