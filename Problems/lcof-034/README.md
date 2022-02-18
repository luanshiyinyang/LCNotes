## 题目描述
给你二叉树的根节点`root`和一个整数目标和`targetSum`，找出所有从**根节点到叶子节点**路径总和等于给定目标和的路径。

## 题解思路
很容易想到递归形式的回溯法进行求解，这里直接上代码，也可见[solve.py](solve.py)。

```python
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> list[list[int]]:
        path, ans = [], []
        def dfs(root, target):
            if not root: return 
            path.append(root.val)
            target -= root.val
            if not root.left and not root.right and target == 0: # 如果满足目标，则将当前路径加入答案中，需要注意的是此处append的是path[:]，而没有直接append(path)，后者会发生path改动，先前加入ans中的解也会发生改动的现象
                ans.append(path[:])
            dfs(root.left, target)
            dfs(root.right, target)
            path.pop() # 将路径最后一个节点弹出，开始尝试下一条路径，这是回溯法的关键，回到之前的状态
        dfs(root, target)
        return ans
```