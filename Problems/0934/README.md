## 题目描述

在给定的二维二进制数组 `A` 中，存在两座岛。（岛是由四面相连的 `1` 形成的一个最大组。）

现在，我们可以将 `0` 变为 `1`，以使两座岛连接起来，变成一座岛。

返回必须翻转的 `0` 的最小数目。（可以保证答案至少是 `1` 。）

**示例1：**

```
输入：A = [[0,1],[1,0]]
输出：1
```

**示例2：**
```
输入：A = [[0,1,0],[0,0,0],[0,0,1]]
输出：2
```

**示例3：**
```
输入：A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
输出：1
```

## 题解思路

我们采用最直观的思路：首先找到这两座岛，随后选择一座，将它不断向外延伸一圈，直到到达了另一座岛。在寻找这两座岛时所在区域，我们使用深度优先搜索；在一座岛向另一座延伸时，我们使用广度优先搜索。

代码如下，也可见于[solve.py](./solve.py)。

```python
class Solution:

    def __init__(self):
        self.dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        res = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    # 开始dfs
                    stack = [(i, j)]
                    seen = set()
                    seen.add((i, j))
                    while stack:
                        node = stack.pop()
                        for nx, ny in self.dirs:
                            newx, newy = node[0] + nx, node[1] + ny
                            if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in seen and grid[newx][newy] == 1:
                                stack.append((newx, newy))
                                seen.add((newx, newy))
                    visited |= seen
                    res.append(seen)

        # 按照题意，这里的res的长度一定是2
        source = res[0]
        queue = collections.deque([(node, 0) for node in source])
        target = res[1]
        while queue:
            node, d = queue.popleft()
            if node in target: return d - 1
            for nx, ny in self.dirs:
                newx, newy = node[0] + nx, node[1] + ny
                if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in source:
                    queue.append(((newx, newy), d + 1))
                    source.add((newx, newy))
```