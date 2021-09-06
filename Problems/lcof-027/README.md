## 题目描述
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：
`root = [4,2,7,1,3,6,9]`

输出：`[4,7,2,9,6,3,1]`

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
```

## 解题思路
当一个节点的两个子树都已经镜像翻转了之后，只需要将这个节点的两个子树交换一下，所以很显然，从根节点开始进行递归遍历。递归的终止条件便为`root`节点为空，说明已经越过了叶子节点。

完整代码如下，详情可见[solve.py](solve.py)

```python
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
```