## 题目描述
有`n`个城市通过一些航班连接。给你一个数组`flights`，其中`flights[i] = [fromi, toi, pricei]`，表示该航班都从城市`fromi`开始，以价格`pricei`抵达`toi`。

现在给定所有的城市和航班，以及出发城市`src`和目的地`dst`，你的任务是找到出一条最多经过`k`站中转的路线，使得从`src`到`dst`的价格最便宜，并返回该价格。如果不存在这样的路线，则输出`-1`。

## 解题思路
这题依旧可以采用动态规划的思路来解决，令`d[t][i]`为从`src`到`i`的途径`t`条路的最短距离，`t=k+1`，经过`k+1`条路便是经过`k`个城市。状态转移较为简单，加入到城市`i`的有`abcd`四个城市，那到城市`i`经过`t`条路的最短距离为，到`abcd`四个城市经过`t-1`条路的距离加上到城市`i`的距离中最短的一个，用公式来写便是：

`d[t][i] = min(d[t-1][j] + cost(j, i))`

其中，`j`为城市`i`的相邻城市。开始状态中，除了`d[0][src]`设为0，其他都设置为`inf`。

完整代码如下，也可见[solve.py](./solve.py)。

```python
class Solution:
    def findCheapestPrice1(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        juli = [[float("inf")] * n for _ in range(k + 2)]
        juli[0][src] = 0
        for t in range(1, k + 2):
            for j, i, cost in flights:
                juli[t][i] = min(juli[t][i], juli[t - 1][j] + cost)
        mincost = min(juli[t][dst] for t in range(1, k + 2))
        if mincost == float("inf"):
            return -1
        else: 
            return mincost
```

## 优化思路

由于`t`的计算只跟`t-1`有关，所以我们可以用两个长度为`n`的列表来代替上述代码中的二维列表。详细代码如下，也可见[solve.py](./solve.py)。
```python
def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        juli1 = [float("inf")] * n 
        juli1[src] = 0
        mincost = float('inf')
        for t in range(1, k + 2):
            juli2 = [float("inf")] * n 
            for j, i, cost in flights:
                juli2[i] = min(juli2[i], juli1[j] + cost)
            juli1 = juli2
            mincost = min(mincost, juli1[dst])
        if mincost == float("inf"):
            return -1
        else: 
            return mincost
```

## 其他解法
显然，这题也可以通过dfs和bfs来解决