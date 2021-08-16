"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(current):
            if not current: return
            dfs(current.left)
            if self.pre != None:
                self.pre.right = current
                current.left = self.pre
            else:
                self.head = current
            self.pre = current
            dfs(current.right)

        if not root: return
        self.pre = None
        dfs(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head