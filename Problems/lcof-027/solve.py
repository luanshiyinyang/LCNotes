class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None: return None
        temp = root.left
        root.left = root.right
        root.right = temp
        if root.left is not None:
            self.mirrorTree(root.left)
        if root.right is not None:
            self.mirrorTree(root.right)
        return root