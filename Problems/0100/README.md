## 题目描述

给你两棵二叉树的根节点 `p` 和 `q` ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

**示例1：**

![](https://i.loli.net/2021/10/10/EGYSP2cfC6brQZp.jpg)

```
输入：p = [1,2,3], q = [1,2,3]
输出：true
```
**示例2：**

![](https://i.loli.net/2021/10/10/6XSDdO1ZhNPHEkB.jpg)

```
输入：p = [1,2], q = [1,null,2]
输出：false
```

**示例3：**

![](https://i.loli.net/2021/10/10/5Pu4zQCYEjSAb3g.jpg)

```
输入：p = [1,2,1], q = [1,1,2]
输出：false
```

## 题解思路

这道题可以采用对称性递归的思路来求解，关于对称性递归的介绍可以参考[我的博文](https://zhouchen.blog.csdn.net/article/details/120684439)。

**边界情况**：两棵树都是空树那么必然相同；
**返回值**：两棵树都非空、根节点值相等、左子树相同、右子树相同。

具体的Python代码如下，也可见于[solve.py](./solve.py)。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        return bool((p and q) and (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
```

上述解法的时间复杂度为$O(min(m, n))$， $m$和$n$分别为两棵树的节点数目。对两个二叉树同时进行深度优先搜索，只有当两个二叉树中的对应节点都不为空时才会访问到该节点，因此被访问到的节点数不会超过较小的二叉树的节点数。

相应的，其空间复杂度为$O(min(m, n))$，空间复杂度取决于递归调用的层数，递归调用的层数不会超过较小的二叉树的最大高度，最坏情况下，二叉树的高度等于节点数。