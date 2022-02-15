class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> list[list[int]]:
        path, ans = [], []
        def dfs(root, target):
            if not root: return 
            path.append(root.val)
            target -= root.val
            if not root.left and not root.right and target == 0:
                ans.append(path[:])
            dfs(root.left, target)
            dfs(root.right, target)
            path.pop()
        dfs(root, target)
        return ans