## 题目描述

设I为一个n位的十进制整数，如果将I分割为k段，则可得到k个整数，这k个整数的乘积称为I的一个k乘积。设计一个算法，对于给定的I和k，求出最大的k乘积。

**示例1：**
```
I=15, k=1
输出15
```

**示例2：**
```
I=12345, k=2
输出6170
```

**示例3：**
```
I=2342, k=2
输出966
```

## 题解思路

这题其实是算法设计里比较经典的K乘积问题，它的解题思路是动态规划算法，最近看到有面试题基于此题魔改的。

首先拿到这道题，我们本能会考虑动态规划，那么一个n位数划分为k段是否与子问题有关呢？我们不妨定义$f(i,j)$来表示前i位数划分为j段的最大K乘积，同时用$L(a,b)$表示从第$a$位开始到第$b$位的十进制数。

假设我们最后一段占用了除前m位数字后的所有数字，那么其实此时的K乘积就等于$f(m,j-1)*L(m, i)$，显然$f(i,j)$具有最优子结构，因此我们只需要在$1\le m \le i$之间枚举所有的m即可，所以有下面的状态转移方程。

$$
f(i,j) = max \{ f(m, j-1) * L(m, i) \} ~~~~~~~ 1\le m \le i
$$

最后补充边界条件，显然前i位数划分为1段，结果就是i位数本身。

因此我们可以写出如下的代码，也可见于[solve.py](./solve.py)。

```python
from typing import List


def cal(num, i, j):
    # 计算num的i位到j位组成的十进制数
    value = 0
    while j >= i:
        value = value * 10 + num[i]
        i = i + 1
    return value


def solve(num: List[int], n, k):
    if k > n:
        return 0
    dp = [[0] * k for _ in range(n)]
    # 对于任何前i位拆为一段，最大乘积都是本身
    for i in range(n):
        dp[i][0] = cal(num, 0, i)

    for j in range(1, k):
        for i in range(j, n):
            dp[i][j] = max([dp[m][j - 1] * cal(num, m + 1, i) for m in range(i)])

    return dp[n - 1][k - 1]


print(solve([2, 3, 4, 2], 4, 2))  # 2342 to 23 * 42

```
