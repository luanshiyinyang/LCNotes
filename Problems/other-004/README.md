## 题目描述

给定一个数字字符串，现在取一个该数字串的子序列（子序列在原串中可以不连续），使得该子序列是9的倍数，子序列可以包含前导零。现在要求计算出有多少个合法的子序列？结果对10^9+7取模。我们定义，若是两个子序列在原串中的位置不同，则认为它们不同。

**示例1：**
```
输入：s = "1188"
输出：5
解释：共有4个不同的"18"子序列和一个"1188"子序列，都是9的倍数。
```

**示例2：**
```
输入：s = "0123"
输出：1
解释：只有子序列"0"是9的倍数。
```

## 题解思路

这题可以很快联想到动态规划，我们定义`dp[i][j]`表示子串s前i个字符构成的子串中对k取余得到的余数是j的子序列的个数。

显然有边界为`dp[0][int(s[0]) % k] = 1`，即到第一个字符构成的子串中，余数为该字符串转为整数对k取余的结果为一个必有方案。

我们推导出一个递推公式，当前的`dp[i][j]`其实有两种情况，一种是当前i位置的字符不选，此时方案数为`dp[i-1][j]`，另一种则为当前方案选，那么要使得余数为j，就应该加上j减去当前位对k余数的方案数，即`dp[i-1][j - m + k]`，通俗来说，就是要想选当前位余数为j，那么只要前面各位的余数加上当前位的余数是k的倍数。注意，这种推导是有条件的，一个数各位数字之和为9的倍数，那么这个数就是9的倍数（同样适用于3，因此这类题一般针对3和9出题）。

$$
dp[i][j] = dp[i-1][j] + dp[i-1][(j-m+k) \% k]
$$

具体的代码如下，也可见于[solve.py](./solve.py)。

```python
class Solution():
    def count_valid_seq(self, s, k=9):
        MOD = int(1e9 + 7)
        n = len(s)
        dp = [[0] * k for _ in range(n)]
        dp[0][int(s[0]) % k] = 1
        for i in range(1, n):
            m = int(s[i]) % k
            dp[i][m] = dp[i][m] + 1
            for j in range(k):
                dp[i][j] += dp[i-1][j] + dp[i-1][(j+k-m) % k]
        return dp[-1][0] % MOD
```
但是，有的时候，方案数会过多，导致计算超时，我们可以dp数组的值就对1e9+7取余来加快运算。

```python
class Solution():
    def count_valid_seq(self, s, k=9):
        MOD = int(1e9 + 7)
        n = len(s)
        dp = [[0] * k for _ in range(n)]
        dp[0][int(s[0]) % k] = 1
        for i in range(1, n):
            m = int(s[i]) % k
            dp[i][m] = (dp[i][m] + 1) % MOD
            for j in range(k):
                dp[i][j] += (dp[i-1][j] + dp[i-1][(j+k-m) % k]) % MOD
        return dp[-1][0] % MOD
```

## 优化思路

当然，本题也可以使用状态压缩来维护一个一维dp数组。

```python
class Solution():
    def count_valid_seq(self, s, k=9):
        MOD = int(1e9 + 7)
        n = len(s)
        dp = [0] * k
        dp[int(s[0]) % k] = 1
        for i in range(1, n):
            dp_raw = dp[:]
            m = int(s[i]) % k
            for j in range(k):
                dp[j] = (dp_raw[j] + dp_raw[(j+k-m) % k]) % MOD
            dp[m] = (dp[m] + 1) % MOD
        return dp[0] % MOD
```
