## 题目描述
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

示例 1：

输入：`root = [1,2,2,3,4,4,3]`

输出：`true`

示例 2：

输入：`root = [1,2,2,null,3,null,3]`

输出：`false`

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
```

## 解题思路
若一棵二叉树是对称的，则对于其根节点来说，需要其两个儿子节点的`val`相等。对于不是根节点的每一对对称节点（`L`和`R`）来说，满足（1）`L.val=R.val`；（2）`L.left.val=R.right.val`；（3）`L.right.val=R.left.val`。由此，我们可以考虑从根节点开始进行递归，判断每一对节点是否对称。终止条件：当`L`和`R`同时越过叶子节点时，此树从顶至底的节点都对称，则返回`true`；当`L`和`R`中只有一个越过了叶子节点，则不对称，返回`false`；当`L`的`val`与`R`的`val`不相等时，不对称，返回`false`。

完整代码如下，也可见[solve.py](solve.py)

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: return True
        def digui(l, r):
            if l is None and r is None: return True
            if l is None or r is None or l.val != r.val: return False
            return digui(l.left, r.right) and digui(l.right, r.left)
        return digui(root.left, root.right)
```
