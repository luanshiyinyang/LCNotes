## 题目描述

树可以看成是一个连通且**无环**的**无向**图。

给定往一棵 `n` 个节点 (节点值 `1～n`) 的树中添加一条边后的图。添加的边的两个顶点包含在 `1` 到 `n` 中间，且这条附加的边不属于树中已存在的边。图的信息记录于长度为 `n` 的二维数组 `edges` ，`edges[i] = [ai, bi]` 表示图中在 `ai` 和 `bi` 之间存在一条边。

请找出一条可以删去的边，删除后可使得剩余部分是一个有着 `n` 个节点的树。如果有多个答案，则返回数组 `edges` 中最后出现的边。

**示例1：**

![](https://s2.loli.net/2022/04/05/Q8EorbKWTCU2tnw.png)

```
输入: edges = [[1,2], [1,3], [2,3]]
输出: [2,3]
```

**示例2：**

![](https://s2.loli.net/2022/04/05/lRpAcJHC4IshG26.png)

```
输入: edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]
```

## 题解思路

正常的n个节点的树会有n-1条边，本题的树会有一条冗余的边。我们知道，树是一个连通且无环的无向图，在树中多了一条边必然会带来环，附加的边就是环出现的原因。

本题可以想到使用并查集来寻找附加的边，思路很清晰：每个节点初始为不同的连通分量。遍历每条边，判断这条边连接的两个顶点是否属于相同的连通分量。
- 若两个顶点属于不同的连通分量，则说明在遍历到当前的边之前，这两个顶点是不连通的，因此当前的边不会导致环，合并这两个顶点的连通分量；
- 若两个顶点属于相同的连通分量，则说明在遍历到当前的边之前，这两个点已经连通，当前的边会导致环的出现，这条边就是我们找的附加边。

代码如下，也可见于[solve.py](./solve.py)。

```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))

        def find(index):
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]
        
        def union(index1, index2):
            parent[find(index1)] = find(index2)

        for node1, node2 in edges:
            if find(node1) != find(node2):
                union(node1, node2)
            else:
                return [node1, node2]
        return []
```

上述解法的时间复杂度为$O(nlogn)$，其中n为节点个数；需要遍历图中的 `n` 条边，对于每条边，需要对两个节点查找祖先，如果两个节点的祖先不同则需要进行合并，需要进行 2 次查找和最多 1 次合并。一共需要进行 2n 次查找和最多 n 次合并，因此总时间复杂度是 $O(2n \log n)=O(n \log n)$。这里的并查集使用了路径压缩，但是没有使用按秩合并，最坏情况下的时间复杂度是 $O(n \log n)$，平均情况下的时间复杂度依然是 $O(n \alpha (n))$，其中 $\alpha$ 为阿克曼函数的反函数，$\alpha (n)$可以认为是一个很小的常数。

空间复杂度为$O(n)$，使用数组parent来记录每个节点的祖先。