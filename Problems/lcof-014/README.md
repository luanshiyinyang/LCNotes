## 题目描述

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

**示例1：**
```
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
```
**示例2：**
```
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
```

补充：这题和主站题库的第343题是相同的，只是换了个说法而已，原题如下。
```
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
```

## 题解思路

这种最优解的问题很容易想到动态规划，但是这题是否适合动态规划呢？我们首先来尝试寻找一个递推关系。

首先，一个正整数n，若n>=2，那么可以将其拆分为两个正整数的和，假定k是第一个数，n-k是第二个数。对n-k，我们可以继续拆分也可以不拆分，但是我们知道，一个正整数的最大乘积一定依赖于比它小的正整数的最大乘积，**因此我们可以考虑采用动态规划来求解**。

我们不妨定义维护的最优解数组dp，其中dp\[i\]表示将正整数i拆分为至少两个数的和之后，这些拆分出来的数的最大乘积。

### 状态初始化

显然，0不是正整数，1也不能拆分为两个正整数的和，因此有`dp[0]=dp[1]=0`。

### 状态转移方程

显然，当i>=2时，假设对i拆分出的第一个正整数为a（必有`1<=a<i`），那么此时存在两种情况：

1. 将i拆分为a和i-a的和，i-a不再进行拆分，此时乘积为a*(i-a)；
2. 将i拆分为a和i-a的和，i-a继续拆分，此时乘积为a*dp[i-a]。

故有，若a固定，状态转移式子为`dp[i] = max(a*(i-a), a*dp[i-a])`，而由于a的范围是1到i-1，因此遍历a得到最大的dp[a]即可，所以总的状态转移方程如下。

$$
d p[i]=\max _{1 \leq a<i}\{\max (a \times(i-a), a \times d p[i-a])\}
$$

### 最优解返回

最终，`dp[n]`就是我们求解的整数n分解的最大乘积。

因此我们可以很轻易写出本题的代码如下，也可以见于[solve.py](./solve.py)。

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(2, n+1):
            for j in range(i):
                dp[i] = max(j*(i-j), j*dp[i-j], dp[i])
        return dp[n]
```

最后不妨看看我们这个略显暴力的DP复杂度是怎么样的，显然，二重遍历对于数字n的复杂度为$O(n^2)$，而维护的dp数组带来的空间复杂度为$O(n)$。

## 优化思路（应对面试）





