# I. 从上到下打印二叉树

## 题目描述

从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

**示例1：**
```
    3
   / \
  9  20
    /  \
   15   7
```
```
[3,9,20,15,7]
```

## 题解思路

非常基础的一个层序遍历，这也叫广度优先遍历（BFS），通常通过队列来实现。

需要注意的是Python中实现队列建议使用`collections`中的`deque`， 其 `popleft()` 方法可达到$O(1)$时间复杂度；列表 `list`的 `pop(0)` 方法时间复杂度为 $O(N)$ 。具体的代码如下。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return res
```

上述解法的时间复杂度为$O(N)$，空间复杂度也为$O(N)$（最差情况下，即当树为平衡二叉树时，最多有 $N/2$ 个树节点同时在 queue 中，使用 $O(N)$ 大小的额外空间。）

# II. 从上到下打印二叉树 II

## 题目描述

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

**示例1：**

```
    3
   / \
  9  20
    /  \
   15   7
```

```
[
  [3],
  [9,20],
  [15,7]
]
```

## 题解思路

这道题和上一题很类似，但是需要将每一行节点分别输出，我们其实可以从结果上看到，输出的顺序是不变的，只是每一行是一个子列表而已。我们依然通过BFS来实现。

代码如下。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()  # deque的popleft复杂度很低，比list的pop低
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res
```

上述解法的时间复杂度为$O(N)$，空间复杂度也为$O(N)$（最差情况下，即当树为平衡二叉树时，最多有 $N/2$ 个树节点同时在 queue 中，使用 $O(N)$ 大小的额外空间。）

# III. 从上到下打印二叉树 III

## 题目描述

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

**示例1：**

```
    3
   / \
  9  20
    /  \
   15   7
```

```
[
  [3],
  [20,9],
  [15,7]
]
```

## 题解思路

这道题其实和上一题差不多，就是每一行换个顺序构建输出队列而已，我们只需要判断当前在奇数行还是偶数行就行，奇数行则正向输出，否则反向。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque([root])
        while queue:
            tmp = collections.deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if len(res) % 2 == 0: tmp.append(node.val)
                else: tmp.appendleft(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(list(tmp))
        return res
```

