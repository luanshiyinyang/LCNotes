
## 题目描述

给定两个字符串`s1`, `s2`，找到使两个字符串相等所需删除字符的ASCII值的最小和。

**示例 1：**
```
输入: s1 = "sea", s2 = "eat"
输出: 231
解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
在 "eat" 中删除 "t" 并将 116 加入总和。
结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
```

**示例 2：**
```
输入: s1 = "delete", s2 = "leet"
输出: 403
解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
```

## 题解思路

这道题和[Leetcode 583](https://leetcode.com/problems/delete-operation-for-two-strings/)类似，不过原来的操作数编程的ascii值而已。

因此，我们不妨定义`dp[i][j]`为s1前i个字符和s2前j个字符的最小ascii和，显然有下面的状态转移方程。

$$
dp[i][j] = dp[i-1][j-1] if s1[i-1] = s2[j-1] \\
dp[i][j] = min(dp[i-1][j] + ascii(s1[i-1]), dp[i][j-1] + ascii(s2[j-1])) if s1[i-1] \ne s2[j-1]
$$

需要注意dp数组的边界初始化，也就是当i为0或者j为0是，dp数组的值为累计ascii值。

代码如下，也可见于[solve.py](./solve.py)。
```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        # 初始状态
        dp[0][0] = 0
        accu = 0
        for i in range(1, m+1):
            accu += ord(s1[i-1])
            dp[i][0] = accu
        accu = 0
        for j in range(1, n+1):
            accu += ord(s2[j-1])
            dp[0][j] = accu
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
        return dp[-1][-1]
```

时间复杂度为$O(mn)$，其中m为`s1`长度，n为`s2`长度。空间复杂度为消耗的dp数组，即为$O(mn)$。