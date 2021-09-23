## 题目描述

给你一个 `m * n` 的网格，其中每个单元格不是 0（空）就是 1（障碍物）。每一步，您都可以在空白单元格中上、下、左、右移动。

如果您 **最多** 可以消除 k 个障碍物，请找出从左上角 `(0, 0)` 到右下角 `(m-1, n-1)` 的最短路径，并返回通过该路径所需的步数。如果找不到这样的路径，则返回 -1。

**示例1：**
```
输入： 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
输出：6
解释：
不消除任何障碍的最短路径是 10。
消除位置 (3,2) 处的障碍后，最短路径是 6 。该路径是 (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
```

**示例2：**
```
输入：
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
输出：-1
解释：
我们至少需要消除两个障碍才能找到这样的路径。
```

## 题解思路

这种二维网格中的最短路问题，通常是BFS（广度优先遍历）来求解，为了避开递归，我们一般借助队列实现。

本题比较麻烦的地方在于，在二维网格中寻找路径的时候，是可以消除一部分障碍物的，这就使得网格发生了变化。但是，实际上我们在行走的过程中也不可能经过一个地方两次，那就是说，“消除”k个障碍物其实等价于“经过”k个障碍物。

不妨用一个三元组来维护搜索的状态，`(x, y, rest)`表示玩家处于`(x, y)`位置且还可以再经过`rest`个障碍物，显然rest的值必须大于0且为整数。根据题意，当前状态`(x, y, rest)`可以向最多四个方向进行搜索，设移动的方向为`(dx, dy)`，那么玩家的下一个新位置就是`(x+dx, y+dy)`。**显然，下面有两种情况，若这个新位置是障碍物，那么新的状态应当为`(x+dx, y+dy, rest-1)`，若这个新位置不是障碍物，那么新的状态为`(x+dx, y+dy, rest)`。** 我们从初始状态`(0, 0, k)`出发，当第一次到达`(m-1, n-1, k')`（k'为非负整数）就得到了从`(0, 0)`到`(m-1,n-1)`且最多经过k个障碍物的最短路径。

本题的优化在于测试用例往往会采用一些非常恶心的用例让你难以AC，因此需要优化搜索空间，题目的k的上限为`m*n`，但是其实考虑一个从左上角到左下角再到右下角的路径，即`(0, 0)`到`(m-1, 0)`再到`(m-1, n-1)`，经过了`m+n-1`个位置，且起点和终点题目已经给出必为0，因此如果选择这条路那么最多只会有`m+n-3`个障碍物，因此可以优化k为原本的k与`m+n-3`的较小者，将BFS复杂度由$(MNK)$降低到$O(MN*min(M+N, K))$。

完整的代码如下，也可见于[solve.py](./solve.py)。
```python
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        k = min(m+n-3, k)
        
        # BFS
        visited, q = set([(0, 0, k)]), collections.deque([(0, 0, k)])
        step = 0
        
        while q:
            step += 1
            cnt = len(q)
            for _ in range(cnt):
                x, y, rest = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 0 and (nx, ny, rest) not in visited:
                            if nx == m - 1 and ny == n - 1:
                                return step
                            q.append((nx, ny, rest))
                            visited.add((nx, ny, rest))
                        elif grid[nx][ny] == 1 and rest > 0 and (nx, ny, rest-1) not in visited:
                            q.append((nx, ny, rest-1))
                            visited.add((nx, ny, rest-1))
        return -1
```

这个解法的时间复杂度和空间复杂度都为$O(MN*min(M+N, K))$。