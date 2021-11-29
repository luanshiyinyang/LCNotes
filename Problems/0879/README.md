## 题目描述
集团里有`n`名员工，他们可以完成各种各样的工作创造利润。

第`i`种工作会产生`profit[i]`的利润，它要求`group[i]`名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。

工作的任何至少产生`minProfit`利润的子集称为盈利计划，并且工作的成员总数最多为`n`。

有多少种计划可以选择？因为答案很大，所以返回结果模`10^9 + 7`的值。

## 题解思路
原本的背包问题为二维（物品和容量限制），此题的限制有两个（已选择的小组员工人数和目前状态的工作获利下限），所以需要三维动态规划来解决，第三维就是可选择的工作。

定义`dp[i][j][k]`为动态规划数组，代表前`i`个工作，选取了`j`个员工，至少获利`k`的盈利计划的总数目。转移方程为：当无法展开工作`i`时，$d p[i][j][k]=d p[i-1][j][k]$；当能够开展工作`i`时，$d p[i][j][k]=d p[i-1][j][k]+d p[i-1][j-\operatorname{group}[i]][\max (0, k-\operatorname{profit}[i])]$。

需要注意的是，这里的最后以为并不是`[k - profit[i]]`，而是`[max(0, k - profit[i])]`。因为`k`是代表利润至少为`k`，所以`k - profit[i]`是有可能为负的，也是合法状态，可是数组中并没有存储[利润为负]这种状态，所以将状态转换到`k=0`的时候，也就是 说“利润至少为负”等价与“利润至少为0”。

代码如下，也可见[solve.py](./solve.py)。
```python
class Solution:
    def profitableSchemes1(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        length = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(length + 1)]
        dp[0][0][0] = 1
        for i in range(1, length + 1):
            g, p = group[i - 1], profit[i - 1]
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    if j < g:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - g][max(0, k - p)]) % (10**9 + 7)
        ans = sum(dp[length][j][minProfit] for j in range(n + 1))
        return ans % (10**9 + 7)
```

## 优化思路
与经典背包问题一样，将三维数组改为二维数组进行优化，代码如下，也可见[solve.py](./solve.py)。
```python
class Solution:
    def profitableSchemes2(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        for i in range(0, n + 1):
            dp[i][0] = 1
        for earn, members in zip(profit, group):
            for j in range(n, members - 1, -1):
                for k in range(minProfit, -1, -1):
                    dp[j][k] = (dp[j][k] + dp[j - members][max(0, k - earn)]) % (10**9 + 7)
        return dp[n][minProfit]
```