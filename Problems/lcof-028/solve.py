class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: return True
        def digui(l, r):
            if l is None and r is None: return True
            if l is None or r is None or l.val != r.val: return False
            return digui(l.left, r.right) and digui(l.right, r.left)
        return digui(root.left, root.right)