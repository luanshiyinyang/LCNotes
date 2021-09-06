class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A is None or B is None: return False
        def digui(A, B):
            if B is None: return True
            if A is None: return False
            if A.val != B.val: return False
            return digui(A.left, B.left) and digui(A.right, B.right)
        return digui(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
