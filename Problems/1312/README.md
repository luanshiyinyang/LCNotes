## 题目描述

给你一个字符串 `s` ，每一次操作你都可以在字符串的任意位置插入任意字符。

请你返回让 `s` 成为回文串的 **最少操作次数** 。

「回文串」是正读和反读都相同的字符串。

**示例 1：**

```
输入：s = "zzazz"
输出：0
解释：字符串 "zzazz" 已经是回文串了，所以不需要做任何插入操作。
```

**示例 2：**

```
输入：s = "mbadm"
输出：2
解释：字符串可变为 "mbdadbm" 或者 "mdbabdm" 。
```

**示例 3：**

```
输入：s = "leetcode"
输出：5
解释：插入 5 个字符后字符串变为 "leetcodocteel" 。
```

**示例 4：**

```
输入：s = "g"
输出：0
```

**示例 5：**

```
输入：s = "no"
输出：1
```

## 题解思路

这其实也是编辑距离类的一道题，并且难度为Hard，是个很棘手的问题。

在确定大致思路时，我们不妨回到字符串本身来思考，如果一个字符串要变成回文串，那么最终最左侧和最右侧的字符一定是相同的。反推一下，若是字符串当前最左侧和最右侧的字符相同，那么就可以继续遍历，若是不同呢？我们进行填补，填补的方式如下。

- 在左侧填补一个最右侧的字符，左侧继续向前遍历；
- 在右侧填补一个最左侧的字符，右侧继续向前遍历。

这两种填补方式都会使得操作数加1，但是想要确定最优解还是需要继续遍历下去，最终得到全局最优解。

上面这个大致的思路显然可以通过**动态规划**来实现，如上所述，若是想要知道区间`[left,right]`之间的最优解，那么可能存在两种情况，即`s[left] == s[right]`和`s[left] != s[right]`。这两种情况分别可以得到两种结果，即`0 + [left + 1, right -1]的最优解`和`1 + min([left+1, right]的最优解, [left, right-1]的最优解)`。

具体来说，我们声明一个`dp[n][n]`的数组，其中`dp[i][j]`表示`s[i:j]`字符串变为回文串的最小操作数，那么显然，有长度为1的字符串操作数为0，也就是说一个字符本身就是回文串，所以我们初始化dp值为全0。边界条件则是若长度为2的区间两个字符不一致，则操作数为1。

递推的过程就是对每个i枚举尾端的j，更新dp数组即可，最终解就是`dp[0][n-1]`。

代码如下，也可见于[solve.py](./solve.py)。
```python
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1):
            dp[i][i+1] = 0 if s[i] == s[i+1] else 1
        
        for i in range(2, n):
            for j in range(n-i):
                if s[j] == s[j+i]:
                    dp[j][j+i] = dp[j+1][j+i-1]
                else:
                    dp[j][j+i] = min(dp[j+1][j+i], dp[j][j+i-1]) + 1
        return dp[0][n-1]
```

上述代码的时间和空间复杂度都是$O(n^2)$，按照经验，dp数组的存储可以进行压缩优化。

## 优化思路

我们可以使用一个一维dp数组来代替原来的二维dp数组，不过由于无法取得所有的历史信息，更新之前要做一个临时存储。

```python
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i in range(n-2, -1, -1):
            pre = 0
            for j in range(i+1, n):
                tmp = dp[j]
                dp[j] = pre if s[i] == s[j] else 1 + min(dp[j], dp[j - 1])
                pre = tmp
        return dp[n-1]
```

空间复杂度从$O(n^2)$降到了$O(n)$，时间复杂度不变。这个优化思路参考了[网站题解](https://leetcode-cn.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/solution/bao-bao-ye-neng-kan-dong-de-leetcode-ti-jie-dp-by-/)，作者的总结如下。

> 这道题的风格可能更偏向于科班一点，特别是其中关于动态规划的部分，包含着满满的套路感。不过我觉得这里面比较重要的部分在于，整个推导过程中前者和后者的关系，也就是如何基于当前值衍生出下一个值。一旦有了这个推导公式，我们便能较为容易的写出对应的代码实现了。