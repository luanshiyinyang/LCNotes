## 题目描述

给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

**示例 1：**

```
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
```

**示例 2：**

```
输入：coins = [2], amount = 3
输出：-1
```

**示例 3：**

```
输入：coins = [1], amount = 0
输出：0
```

**示例 4：**

```
输入：coins = [1], amount = 1
输出：1
```

**示例 5：**

```
输入：coins = [1], amount = 2
输出：2
```

## 题解思路

首先这道题做个概括，“选物品”、“每个物品无限件”、“求最优值”，我们会很敏感的归纳出这是一个**完全背包**问题，那么我们就可以套模板直接做了。

我们设`dp[i][j]`表示前i种硬币凑为金额j所需的最少硬币个数，显然有下面的递推关系，其中$w_i$表示第i种硬币的面值。

$$
fp[i, j] = min(dp[i-1, j], dp[i, j-w_i] + 1)
$$

因此我们得出下面的代码，也可见于[solve.py](./solve.py)。

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] = min(dp[j], dp[j-coins[i]] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1
```

上述解法的时间复杂度为$O(Sn)$，其中$S$为金额，$n$是面额数；空间复杂度为$O(S)$。