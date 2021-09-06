## 题目描述
输入两棵二叉树`A`和`B`，判断`B`是不是`A`的子结构，（约定空树不是任意一个树的子结构）。`B`是`A`的子结构，即`A`中有出现和`B`相同的结构和节点值。

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
```

## 解题思路
若树`B`是树`A`的子结构，则子结构的根节点可能是树`A`的任意一个节点。因此，判断树`B`是树`A`的子结构需要分为两步，首先遍历树`A`的每一个节点`a`，再判断树`A`中节点`a`的子树是否和树`B`一样。所以代码中需要两个递归过程。

完整代码如下，也可见[solve.py](solve.py)。
```python
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A is None or B is None: return False
        def digui(A, B):
            if B is None: return True
            if A is None: return False
            if A.val != B.val: return False
            return digui(A.left, B.left) and digui(A.right, B.right)
        return digui(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
```
其中的`digui`函数便是判断以树`A`中的某个节点`a`为根节点的结构是否与树`B`相同，其递归的终止条件为：当树`B`越过了叶子节点，说明树`B`完全匹配，所以返回`true`；当树`A`为空，说明越过叶子节点，匹配失败，返回`true`；当两者的`val`不同，匹配失败，返回`false`。整个的`isSubStructure`函数其实就是对二叉树做一个先序遍历。