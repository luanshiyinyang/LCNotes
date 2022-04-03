## 题目描述

地图上有 `m` 条无向边，每条边 `(x, y, w)` 表示位置 `x` 到位置 `y` 的权值为 `w`。从位置 `0` 到 位置 `n` 可能有多条路径。我们定义一条路径的危险值为这条路径中所有的边的最大权值。

请问从位置 `0` 到 位置 `n` 所有路径中最小的危险值为多少？

**示例1：**

```
给出 n = `2`, m = `2`, x = `[0, 1]`, y = `[1, 2]`, w = `[1, 2]`，返回`2`。
输入:
2
2
[0,1]
[1,2]
[1,2]
输出:
2

解释：
路径 1：0->1->2（危险值：2）
最小危险值为2。
```

**示例2：**

```
给出 n = `3`, m = `4`, x = `[0, 0, 1, 2]`, y = `[1, 2, 3, 3]`, w = `[1, 2, 3, 4]`，返回`3`。
输入:
3
4
[0,0,1,2]
[1,2,3,3]
[1,2,3,4]
输出:
3

解释：
路径 1：0->1->3（危险值：3）
路径 2：0->2->3（危险值：4）
最小危险值为3。
```

**示例3：**

```
给出 n = `4`, m = `5`, x = `[0, 1, 1, 2, 3]`, y = `[1, 2, 3, 4, 4]`, w = `[3, 2, 4, 2, 1]`，返回`3`。
输入:
4
5
[0,1,1,2,3]
[1,2,3,4,4]
[3,2,4,2,1]
输出:
3

解释：
路径 1：0->1->2->4（危险值：3）
路径 2：0->1->3->4（危险值：4）
最小危险值为3。
```

**示例4：**

```
给出 n = `5`, m = `7`, x = `[0, 0, 1, 2, 3, 3, 4]`, y = `[1, 2, 3, 4, 4, 5, 5]`, w = `[2, 5, 3, 4, 3, 4, 1]`，返回`3`。
输入:
5
7
[0,0,1,2,3,3,4]
[1,2,3,4,4,5,5]
[2,5,3,4,3,4,1]
输出:
3

解释：
路径 1：0->1->3->5（危险值：4）
路径 2：0->1->3->4->5（危险值：3）
路径 3：0->2->4->3->5（危险值：5）
路径 4：0→2->4→5（危险值：5）
最小危险值为3。
```

## 题解思路

这道题其实就求最小生成树中0到n路径上的最大边权。为了得到最小生成树，我们可以采用Prim算法来求解。

这里回顾一下Prim算法，分为如下四个步骤。
1. 输入一个加权连通图，其中顶点集合为$V$，边集合为$E$；
2. 初始化$V_{new} = \{x\}$，其中$x$为集合$V$中的任一顶点（起始点），$E_{new} = \{\}$为空；
3. 重复以下操作直到$V_{new} = V$：
   1. 在集合$E$中选取权值最小的边`<u, v>`，其中$u$为集合$V_{new}$中的元素，而$v$不在$V_{new}$中，并且$v \in V$（如果存在有多条满足上述条件且具有相同权值的边，则可以任选其中之一）；
   2. 将$v$加入$V_{new}$中，同时将边`<u, v>`加入$E_{new}$中。
4. 输出$V_{new}$和$E_{new}$构成的最小生成树。

本题求解的代码如下，也可见于[solve.py](./solve.py)。

```python
class Solution:
    """
    @param n: maximum index of position.
    @param m: the number of undirected edges.
    @param x: 
    @param y: 
    @param w: 
    @return: return the minimum risk value.
    """
    def get_min_risk_value(self, n: int, m: int, x: List[int], y: List[int], w: List[int]) -> int:
        # 建图
        adj = collections.defaultdict(list)
        for i in range(m):
            adj[x[i]].append((y[i], w[i]))
            adj[y[i]].append((x[i], w[i]))
        print(adj)
        MST = collections.defaultdict(list)
        min_heap = [(w, 0, v) for v, w in adj[0]]
        heapq.heapify(min_heap)

        while n not in MST:
            w, p, v = heapq.heappop(min_heap)
            if v not in MST:
                MST[p].append((v, w))
                MST[v].append((p, w))
                for k, w in adj[v]:
                    if k not in MST:
                        heapq.heappush(min_heap, (w, v, k))
        
        dfs = [(0, None, float('-inf'))]
        while dfs:
            v, p, max_w = dfs.pop()
            for k, w in MST[v]:
                cur_max_w = max(max_w, w)
                if k == n:
                    return cur_max_w
                if k != p:
                    dfs.append((k, v, cur_max_w))
```