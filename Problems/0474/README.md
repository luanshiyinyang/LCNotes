## 题目描述
给你一个二进制字符串数组`strs`和两个整数`m`和`n`。

请你找出并返回`strs`的最大子集的长度，该子集中**最多**有`m`个0和`n`个1。

如果`x`的所有元素也是`y`的元素，集合`x`是集合`y`的**子集**。

**示例:**
```
输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有5个0和3个1的最大子集是{"10","0001","1","0"}，因此答案是4。
其他满足题意但较小的子集包括{"0001","1"}和{"10","1","0"}。{"111001"}不满足题意，因为它含4个1，大于n的值3。
```

## 题解思路
较明显地看出这是两重约束的背包问题，在0和1的个数有限制的情况下，尽可能多地选取字符串。最简单的背包问题可以用二维动态规划解决，这题则需要三重动态规划。

定义三维数组`dp[s][i][j]`， 代表前`s`个字符串中，在0的个数少于`i`且1的个数少于`j`的情况下，最多选取的字符串个数最终结果则为`dp[l][m][n]`。

当字符串个数`s`为0时，很显然均需要初始化为0。其转移方程为：
$$d p[i][j][k]= \begin{cases}d p[i-1][j][k], & j<\text { zeros } \mid k<\text { ones } \\ \max (d p[i-1][j][k], d p[i-1][j-\text { zeros }][k-\text { ones }]+1), & j \geq \text { zeros } \& k \geq \text { ones }\end{cases}$$

代码如下，也可见[solve.py](./solve.py)。
```python
class Solution:
    def findMaxForm1(self, strs: List[str], m: int, n: int) -> int:
        k = len(strs)
        if m == 0 and n == 0: return 0
        dp = [[[False] * (n + 1) for _ in range(m + 1)] for __ in range(k + 1)]
        for s in range(k+1):
            dp[s][0][0] = 0
        for i in range(m+1):
            for j in range(n+1):
                dp[0][i][j] = 0
        for s in range(1, k+1):
            for i in range(m + 1):
                for j in range(n + 1):
                    nums0, nums1 = self.count(strs[s - 1])
                    if nums0 <= i and nums1 <= j:
                        dp[s][i][j] = max(dp[s - 1][i][j], dp[s - 1][i - nums0][j - nums1] + 1)
                    else:
                        dp[s][i][j] = dp[s - 1][i][j]
        return dp[k][i][j]
```

## 优化思路
背包问题的优化思路：不难发现在循环更新的时候`dp[s]`这一次循环只与`dp[s-1]`这一层有关，所以我们可以构建一个`dp[i][j]`的数组即可，不过此时需要将循环逆序，以保证访问到当前元素时，其并没有被更新过。

代码如下，也可见[solve.py](./solve.py)。
```python
class Solution:
    def findMaxForm2(self, strs: List[str], m: int, n: int) -> int:
        k = len(strs)
        if m == 0 and n == 0: return 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        for s in range(1, k + 1):
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    nums0, nums1 = self.count(strs[s - 1])
                    if nums0 <= i and nums1 <= j:
                        dp[i][j] = max(dp[i][j], dp[i - nums0][j - nums1] + 1)
        return dp[m][n]
```