## 题目描述

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

```python
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## 题解思路

作为为数不多的菜鸟之一，第一眼看到这个题目的反应是不会。但其实仔细一想，其实就是按序遍历二叉搜索树，并在遍历的过程中将节点进行两个方向的连接。转换后的循环双向链表是递增的，所以需要将二叉搜索树进行中序遍历（左子树，根节点，右子树的顺序）。

## 算法流程

首先初始化self.pre和self.head两个空节点。self.head指向的就是中序遍历中的第一个节点，self.pre指向上一次遍历的节点。

dfs(current)：对当前节点进行深度优先遍历。
1. 当current为空时，说明已经越过了叶子节点，直接返回；
2. 对current左子树进行递归遍历，dfs(current.left)；
3. 当self.pre为空时，说明此时访问的是第一个节点，将self.head指向该节点；当self.pre不为空时，修改节点两个方向的指向；将current节点保存为pre节点；
4. 对current的右子树进行递归遍历，dfs(current.right);

遍历结束后self.head和self.pre分别指向链表的头结点和尾结点，再将头尾节点连接起来，最终返回self.head。


完整代码见[solve.py](./solve.py)。maple