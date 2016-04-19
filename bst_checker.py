class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def bst_checker(root, lower_bound=-float('inf'), upper_bound=float('inf')):
    """Use recursion to check if a binary tree is a valid binary search tree."""

    if not root:
        return True

    if root.value < lower_bound or root.value > upper_bound:
        return False

    return bst_checker(root.left, lower_bound, root.value) and bst_checker(root.right, root.value, upper_bound)
