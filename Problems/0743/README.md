## 题目描述

有 `n` 个网络节点，标记为 `1` 到 `n`。

给你一个列表 `times`，表示信号经过 **有向** 边的传递时间。 `times[i] = (ui, vi, wi)`，其中 `ui` 是源节点，`vi` 是目标节点， `wi` 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 `K` 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 `-1` 。

**示例1：**

![](https://s2.loli.net/2022/04/03/YUH7MbBV5qrQk4m.png)
```
输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
输出：2
```

**示例2：**

```
输入：times = [[1,2,1]], n = 2, k = 1
输出：1
```

**示例3：**

```
输入：times = [[1,2,1]], n = 2, k = 2
输出：-1
```

## 题解思路

这题是典型的单源最短路径问题，根据题意，从节点 `k` 发出的信号，到达节点 `x` 的时间就是节点 `k` 到节点 `x` 的最短路的长度。因此我们需要求出节点 `k` 到其余所有点的最短路，其中的最大值就是答案。若存在从 `k` 出发无法到达的点，则返回 `−1`。

我们采用Dijkstra算法来求解本题，我们回顾该算法，其主要思想是贪心。

> 将所有节点分成两类：已确定从起点到当前点的最短路长度的节点，以及未确定从起点到当前点的最短路长度的节点（下面简称「未确定节点」和「已确定节点」）。

> 每次从「未确定节点」中取一个与起点距离最短的点，将它归类为「已确定节点」，并用它「更新」从起点到其他所有「未确定节点」的距离。直到所有点都被归类为「已确定节点」。

> 用节点 A「更新」节点 B 的意思是，用起点到节点 A 的最短路长度加上从节点 A 到节点 B 的边的长度，去比较起点到节点 B 的最短路长度，如果前者小于后者，就用前者更新后者。这种操作也被叫做「松弛」。

> 这里暗含的信息是：每次选择「未确定节点」时，起点到它的最短路径的长度可以被确定。

> 可以这样理解，因为我们已经用了每一个「已确定节点」更新过了当前节点，无需再次更新（因为一个点不能多次到达）。而当前节点已经是所有「未确定节点」中与起点距离最短的点，不可能被其它「未确定节点」更新。所以当前节点可以被归类为「已确定节点」。

为了挑选距离起点最短的点，因此我们可以使用小根堆来便于查询。

完整的代码如下，也可见于[solve.py](./solve.py)。

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = collections.defaultdict(list)
        for start, end, time in times:
            g[start].append((end, time))
        
        # 生成最短路径树SPT
        SPT = {}
        min_heap = [(0, k)]
        while min_heap:
            duration, node = heappop(min_heap)
            if node not in SPT:
                SPT[node] = duration
                for adj_node, adj_node_duration in g[node]:
                    if adj_node not in SPT:
                        heappush(min_heap, (adj_node_duration + duration, adj_node))
        return max(SPT.values()) if len(SPT) == n else -1
```