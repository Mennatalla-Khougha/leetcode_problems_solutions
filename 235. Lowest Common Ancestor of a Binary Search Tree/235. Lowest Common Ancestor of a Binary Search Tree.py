class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    Find the lowest common ancestor of two nodes in a Binary Search Tree (BST).

    Parameters:
    - root ('TreeNode'): The root of the BST.
    - p ('TreeNode'): A node in the BST.
    - q ('TreeNode'): Another node in the BST.

    Returns:
    - 'TreeNode': The lowest common ancestor of nodes p and q.
    """
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
