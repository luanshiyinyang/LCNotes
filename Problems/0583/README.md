## 题目描述

给定两个单词 `word1` 和 `word2`，找到使得 `word1` 和 `word2` 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

**示例1：**
```
输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
```

## 题解思路

这题也是编辑距离的经典题型，还是按照两个指针i和j分别指向两个字符串的最后，一步步向前走缩小问题的规模。

本题如何考虑呢？很简单，不妨先设`dp[i][j]`表示word1前i个字符串和word2前j个字符串之间匹配的最小删除次数，显然当两个指针访问到`word1[i]`和`word2[j]`的时候，有下面两种情况：
- 若`word[i] == word[j]`，则两个字符匹配，无需删除字符，i和j同时前移，也就是`dp[i][i]=dp[i-1][j-1]`。
- 若`word1[i]`和`word2[j]`不匹配，那么就需要考虑删除哪个字符了，删除的同时操作数加1。很显然，我们只需要选择`dp[i-1][j]`和`dp[i][j-1`中较小的那个即可。

上述过程的代码实现如下，也可见于[solve.py](./solve.py)。

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
```

显然，上述解法的时间和空间复杂度都是$O(mn)$，其中m为word1长度，n为word2长度。

## 优化思路

本题可以进一步优化，在上述的求解过程中，其实对于最优解数组而言，只涉及到了DP Table的当前行和上一行，因此只需要维护这两行即可。我们用dp数组来记录上一行的解，用temp数组来更新当前行的解，temp求解完成后更新到dp上即可。

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [0] * (n+1)
        
        for i in range(m+1):
            temp = [0] * (n+1)
            for j in range(n+1):
                if i == 0 or j == 0:
                    temp[j] = i + j
                elif word1[i-1] == word2[j-1]:
                    temp[j] = dp[j-1]
                else:
                    temp[j] = 1 + min(dp[j], temp[j-1])
            dp = temp
        return dp[n]
```
此时时间复杂度不变，空间复杂度优化为$O(n)$。
